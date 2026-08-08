const DEMO_MENU = {
  menu_id: "demo_menu_001",
  version: 1,
  items: [
    { program: "Classic", day: 1, meal: "Завтрак", dish_id: "z1", name: "Овсяная каша с ягодами", desc: "Овсяные хлопья, свежие ягоды, мёд", portions: 1, price: 120, weight: 250, tags: "" },
    { program: "Classic", day: 1, meal: "Обед", dish_id: "o1", name: "Куриный суп с лапшой", desc: "Куриный бульон, лапша, морковь, зелень", portions: 1, price: 180, weight: 350, tags: "" },
    { program: "Classic", day: 1, meal: "Ужин", dish_id: "u1", name: "Гречка с котлетой", desc: "Гречневая каша, куриная котлета, салат", portions: 1, price: 220, weight: 300, tags: "" },
    { program: "Classic", day: 1, meal: "Перекус", dish_id: "p1", name: "Творожная запеканка", desc: "Творог, изюм, ваниль", portions: 1, price: 90, weight: 150, tags: "" },

    { program: "Classic", day: 2, meal: "Завтрак", dish_id: "z2", name: "Блины с творогом", desc: "Тонкие блины, творожная начинка", portions: 1, price: 140, weight: 220, tags: "" },
    { program: "Classic", day: 2, meal: "Обед", dish_id: "o2", name: "Борщ", desc: "Свекольный суп, сметана, чесночные сухарики", portions: 1, price: 190, weight: 350, tags: "" },
    { program: "Classic", day: 2, meal: "Ужин", dish_id: "u2", name: "Рыба запечённая с овощами", desc: "Треска, брокколи, морковь, лимон", portions: 1, price: 250, weight: 300, tags: "" },
    { program: "Classic", day: 2, meal: "Перекус", dish_id: "p2", name: "Йогурт с орехами", desc: "Натуральный йогурт, грецкие орехи", portions: 1, price: 80, weight: 150, tags: "" },

    { program: "Balance", day: 1, meal: "Завтрак", dish_id: "zb1", name: "Омлет с овощами", desc: "Яйца, помидоры, перец, шпинат", portions: 1, price: 130, weight: 200, tags: "" },
    { program: "Balance", day: 1, meal: "Обед", dish_id: "ob1", name: "Тёплый салат с курицей", desc: "Грудка, авокадо, помидоры, оливковое масло", portions: 1, price: 210, weight: 300, tags: "" },
    { program: "Balance", day: 1, meal: "Ужин", dish_id: "ub1", name: "Лосось на пару", desc: "Лосось, спаржа, коричневый рис", portions: 1, price: 280, weight: 280, tags: "" },
    { program: "Balance", day: 1, meal: "Перекус", dish_id: "pb1", name: "Протеиновый коктейль", desc: "Протеин, банан, миндальное молоко", portions: 1, price: 100, weight: 300, tags: "" },

    { program: "Vegan", day: 1, meal: "Завтрак", dish_id: "zv1", name: "Гранола с растительным молоком", desc: "Гранола, миндальное молоко, банан", portions: 1, price: 110, weight: 250, tags: "" },
    { program: "Vegan", day: 1, meal: "Обед", dish_id: "ov1", name: "Том ям с тофу", desc: "Кокосовое молоко, тофу, грибы, лемонграсс", portions: 1, price: 200, weight: 350, tags: "" },
    { program: "Vegan", day: 1, meal: "Ужин", dish_id: "uv1", name: "Вок с овощами и нутом", desc: "Брокколи, морковь, нут, соевый соус", portions: 1, price: 190, weight: 300, tags: "" },
    { program: "Vegan", day: 1, meal: "Перекус", dish_id: "pv1", name: "Хумус с овощными палочками", desc: "Нут, тахини, морковь, огурец", portions: 1, price: 85, weight: 180, tags: "" },
  ],
  tariffs: [
    { program: "Classic", people: 1, weekly_price: 1650 },
    { program: "Classic", people: 2, weekly_price: 3000 },
    { program: "Balance", people: 1, weekly_price: 1950 },
    { program: "Balance", people: 2, weekly_price: 3600 },
    { program: "Vegan", people: 1, weekly_price: 1500 },
    { program: "Vegan", people: 2, weekly_price: 2800 },
  ],
  settings: { child_ratio: 0.5, discount_7days: 10 }
};

function demoCalc(groups, days, startDay) {
  const allResults = [];

  groups.forEach(group => {
    const prog = group.program;
    const adults = group.adults || 0;
    const children = group.children || 0;
    const peopleEquiv = adults + children * 0.5;
    const totalPeople = adults + children;

    const tariff = DEMO_MENU.tariffs.find(t => t.program === prog && t.people === Math.round(peopleEquiv));
    let kitPrice;
    if (tariff) {
      kitPrice = (tariff.weekly_price / 7) * days;
    } else {
      const items = DEMO_MENU.items.filter(i => i.program === prog);
      const dayCost = items.reduce((sum, i) => sum + i.price * i.portions * peopleEquiv, 0);
      kitPrice = dayCost * days;
    }

    const plan = [];
    for (let d = 0; d < days; d++) {
      const dayNum = ((startDay - 1 + d) % 7) + 1;
      const dayItems = DEMO_MENU.items.filter(i => i.program === prog && i.day <= 2);
      const meals = {};
      dayItems.forEach(item => {
        if (!meals[item.meal]) meals[item.meal] = [];
        meals[item.meal].push({
          "Название_блюда": item.name,
          "Описание": item.desc,
          "Цена_за_порцию": item.price,
          "Порции_на_человека": item.portions,
          "Стоимость_строки": Math.round(item.price * item.portions * peopleEquiv),
          "Вес_грамм": item.weight,
          "Теги": item.tags
        });
      });
      const mealOrder = ["Завтрак", "Обед", "Ужин", "Перекус"];
      const приёмы = mealOrder.filter(m => meals[m]).map(m => ({
        "Приём": m,
        "блюда": meals[m]
      }));
      const dayCost = приёмы.reduce((s, m) => s + m.блюда.reduce((bs, b) => bs + b["Стоимость_строки"], 0), 0);
      plan.push({ "День": dayNum, "приёмы": приёмы, "дневная_стоимость": dayCost });
    }

    allResults.push({
      program: prog,
      adults: adults,
      children: children,
      people_equiv: peopleEquiv,
      computed_price: kitPrice / days,
      kit_price: Math.round(kitPrice),
      plan: plan
    });
  });

  const totalKit = allResults.reduce((s, g) => s + g.kit_price, 0);
  const totalPeople = allResults.reduce((s, g) => s + g.adults + g.children, 0);
  const discountPercent = days >= 7 ? 10 : 0;
  const discountAmount = Math.round(totalKit * discountPercent / 100);
  const finalPrice = totalKit - discountAmount;

  return {
    menu_id: "demo_menu_001",
    token: "demo_" + Math.random().toString(36).slice(2, 10),
    groups: allResults,
    days: days,
    start_day: startDay,
    per_day_cost: Math.round(finalPrice / days),
    total_kit_price: totalKit,
    discount_percent: discountPercent,
    discount_amount: discountAmount,
    final_price: finalPrice,
    per_person_per_day: totalPeople > 0 ? Math.round(finalPrice / totalPeople / days) : 0
  };
}
