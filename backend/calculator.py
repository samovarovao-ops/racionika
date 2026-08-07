from backend.menu_parser import MenuData
from backend.models.schemas import CalcResult, GroupResult, DayPlan, DayMeal

DEFAULT_CHILD_PORTION_RATIO = 0.5
DEFAULT_ROUNDING = 1
VALID_PROGRAMS = {"Classic", "Balance", "Vegan"}


def _calculate_single_group(menu_data: MenuData, program: str, adults: int, children: int,
                            days: int, start_day: int, child_ratio: float, rounding: int) -> GroupResult:
    if program not in VALID_PROGRAMS:
        raise ValueError(f"Invalid program: {program}. Valid: {', '.join(sorted(VALID_PROGRAMS))}")
    if adults < 0:
        raise ValueError("Adults must be >= 0")
    if children < 0:
        raise ValueError("Children must be >= 0")
    if adults + children < 1:
        raise ValueError("At least 1 person required per group")

    children_equiv = children * child_ratio
    people_equiv = adults + children_equiv

    selected_days = []
    for i in range(days):
        d = ((start_day - 1 + i) % 7) + 1
        selected_days.append(d)

    plan = []
    computed_price = 0.0

    for day_num in selected_days:
        day_items = [
            item for item in menu_data.menu_items
            if item.Программа == program and item.День == day_num
        ]

        day_cost = 0.0
        meal_groups = {}
        for item in day_items:
            if item.Приём not in meal_groups:
                meal_groups[item.Приём] = []
            meal_groups[item.Приём].append(item)

        day_meals = []
        meal_order = ["Завтрак", "Обед", "Ужин", "Перекус"]
        for meal_name in meal_order:
            if meal_name not in meal_groups:
                continue
            items = meal_groups[meal_name]
            bludo_list = []
            for item in items:
                row_cost = item.Цена_за_порцию * item.Порции_на_человека * people_equiv
                row_cost = round(row_cost, rounding)
                day_cost += row_cost
                bludo_list.append({
                    "Название_блюда": item.Название_блюда,
                    "Описание": item.Описание,
                    "Цена_за_порцию": item.Цена_за_порцию,
                    "Порции_на_человека": item.Порции_на_человека,
                    "Стоимость_строки": row_cost,
                    "Вес_грамм": item.Вес_грамм,
                    "Теги": item.Теги,
                    "Блюдо_ID": item.Блюдо_ID,
                })
            day_meals.append(DayMeal(Приём=meal_name, блюда=bludo_list))

        day_cost = round(day_cost, rounding)
        computed_price += day_cost
        plan.append(DayPlan(День=day_num, приёмы=day_meals, дневная_стоимость=day_cost))

    computed_price = round(computed_price, rounding)

    kit_price = computed_price
    if people_equiv == int(people_equiv):
        rounded_people = int(people_equiv)
        for tariff in menu_data.tariffs:
            if tariff.Программа == program and tariff.Люди == rounded_people:
                kit_price = tariff.Цена_за_неделю
                break

    return GroupResult(
        program=program,
        adults=adults,
        children=children,
        people_equiv=people_equiv,
        computed_price=computed_price,
        kit_price=kit_price,
        plan=plan,
    )


def calculate(menu_data: MenuData, groups: list, days: int, start_day: int = 1) -> CalcResult:
    if days < 1 or days > 7:
        raise ValueError("Days must be 1..7")
    if not groups:
        raise ValueError("At least 1 group required")

    rounding = int(menu_data.settings.get("rounding", DEFAULT_ROUNDING))
    currency = menu_data.settings.get("currency", "RUB")
    child_ratio = float(menu_data.settings.get("child_portion_ratio", DEFAULT_CHILD_PORTION_RATIO))

    group_results = []
    total_computed = 0.0
    total_kit = 0.0
    total_people = 0

    for g in groups:
        program = g.program if hasattr(g, 'program') else g.get('program', '')
        adults = g.adults if hasattr(g, 'adults') else g.get('adults', 0)
        children = g.children if hasattr(g, 'children') else g.get('children', 0)

        gr = _calculate_single_group(menu_data, program, adults, children, days, start_day, child_ratio, rounding)
        group_results.append(gr)
        total_computed += gr.computed_price
        total_kit += gr.kit_price
        total_people += adults + children

    total_computed = round(total_computed, rounding)
    total_kit = round(total_kit, rounding)

    per_person_per_day = round(total_kit / total_people / days, rounding) if total_people > 0 and days > 0 else 0
    per_day_cost = round(total_kit / days, rounding) if days > 0 else 0

    discount_percent = 10.0 if days == 7 else 0.0
    discount_amount = round(total_kit * discount_percent / 100, rounding)
    final_price = round(total_kit - discount_amount, rounding)

    return CalcResult(
        menu_id="",
        groups=group_results,
        days=days,
        start_day=start_day,
        total_computed_price=total_computed,
        total_kit_price=total_kit,
        total_people=total_people,
        per_person_per_day=per_person_per_day,
        per_day_cost=per_day_cost,
        discount_percent=discount_percent,
        discount_amount=discount_amount,
        final_price=final_price,
        currency=currency,
    )
