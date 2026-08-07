# -*- coding: utf-8 -*-
import os
import logging
import traceback
import httpx
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, MessageHandler, CallbackQueryHandler,
    filters, ContextTypes
)

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
API_BASE = os.getenv("API_BASE", "http://localhost:8000")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID", "")

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

PROGS = {"Classic": "Классика", "Balance": "Баланс", "Vegan": "Веган"}
PROG_LIST = ["Classic", "Balance", "Vegan"]


def fmt(v):
    return f"{round(v):,}".replace(",", " ")


async def api_get(path, params=None):
    try:
        async with httpx.AsyncClient() as c:
            r = await c.get(f"{API_BASE}{path}", params=params, timeout=30)
            if r.status_code != 200:
                logger.error(f"API GET {path} {r.status_code}")
                return None
            return r.json()
    except Exception as e:
        logger.error(f"API GET {path}: {e}")
        return None


async def api_post(path, data):
    try:
        async with httpx.AsyncClient() as c:
            r = await c.post(f"{API_BASE}{path}", json=data, timeout=30)
            if r.status_code != 200:
                logger.error(f"API POST {path} {r.status_code}: {r.text[:200]}")
                return None
            return r.json()
    except Exception as e:
        logger.error(f"API POST {path}: {e}")
        return None


def person_keyboard():
    buttons = []
    for prog_key, prog_label in PROGS.items():
        buttons.append([
            InlineKeyboardButton(f"{prog_label}: Взрослый", callback_data=f"p_{prog_key}_a"),
            InlineKeyboardButton(f"{prog_label}: Ребёнок", callback_data=f"p_{prog_key}_c"),
        ])
    return InlineKeyboardMarkup(buttons)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()
    args = context.args
    if args and args[0].startswith("share_"):
        token = args[0][6:]
        data = await api_get(f"/api/share/{token}")
        if not data:
            await update.message.reply_text("Результат не найден или устарел.")
            return
        context.user_data["shared_calc"] = data
        await show_result(update, context, data)
        return

    await update.message.reply_text(
        "Рационика — Интеллектуальный калькулятор рационов\n\n"
        "/calc — пошаговый расчёт\n"
        "/orders — мои заказы\n"
        "/site — открыть сайт"
    )


async def calc_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.replace("/calc", "").strip()
    if text:
        parts = text.split()
        program = parts[0]
        if program not in PROG_LIST:
            await update.message.reply_text("Программа: Classic | Balance | Vegan")
            return
        adults = int(parts[1]) if len(parts) > 1 else 1
        children = int(parts[2]) if len(parts) > 2 else 0
        days = int(parts[3]) if len(parts) > 3 else 7
        await do_calc(update, context, [{"program": program, "adults": adults, "children": children}], days)
        return

    context.user_data.clear()
    context.user_data["groups"] = []
    context.user_data["awaiting"] = "count"
    await update.message.reply_text("Сколько людей в расчёте?")


async def my_orders(update: Update, context: ContextTypes.DEFAULT_TYPE):
    orders = await api_get("/api/orders")
    if not orders:
        await update.message.reply_text("Заказов пока нет.")
        return
    my = [o for o in orders if o.get("source") == "telegram"]
    if not my:
        await update.message.reply_text("Заказов через бота пока нет.")
        return
    status_text = {"pending": "Ожидает", "confirmed": "Подтверждён", "cancelled": "Отменён"}
    lines = []
    for o in my[-5:]:
        s = status_text.get(o.get("status", ""), "Неизвестен")
        lines.append(f"#{o['order_id'][:8]} — {o.get('days', '?')} дн. — {s}")
    await update.message.reply_text("Ваши заказы:\n\n" + "\n".join(lines))


async def site_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    btn = InlineKeyboardButton("Открыть сайт", url="http://127.0.0.1:3000")
    await update.message.reply_text("Калькулятор рационов:", reply_markup=InlineKeyboardMarkup([[btn]]))


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await _handle_message(update, context)
    except Exception as e:
        logger.error(f"handle_message error: {e}\n{traceback.format_exc()}")
        await update.message.reply_text("Произошла ошибка. Попробуйте /start")


async def _handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    awaiting = context.user_data.get("awaiting")
    text = update.message.text
    logger.info(f"MSG from {update.effective_user.id}: '{text}', state={awaiting}")

    if awaiting == "count":
        try:
            count = max(1, min(10, int(text)))
        except ValueError:
            await update.message.reply_text("Введите число от 1 до 10:")
            return
        context.user_data["total"] = count
        context.user_data["groups"] = []
        context.user_data["person_idx"] = 0
        context.user_data["awaiting"] = "person"
        await update.message.reply_text(
            f"Человек 1 из {count}. Выберите:",
            reply_markup=person_keyboard()
        )

    elif awaiting == "days":
        try:
            days = max(1, min(7, int(text)))
        except ValueError:
            await update.message.reply_text("Введите число от 1 до 7:")
            return
        context.user_data["awaiting"] = None
        groups = context.user_data.get("groups", [])
        logger.info(f"Ready to calc: groups={groups}, days={days}")
        await do_calc(update, context, groups, days)

    else:
        logger.info(f"No state, ignoring message '{text}'")


async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await _handle_callback(update, context)
    except Exception as e:
        logger.error(f"handle_callback error: {e}\n{traceback.format_exc()}")
        query = update.callback_query
        await query.answer("Ошибка")


async def _handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data
    logger.info(f"CB from {query.from_user.id}: data={data}")

    if data == "noop":
        await query.answer()
        return

    if data.startswith("p_"):
        await query.answer()
        parts = data.split("_")
        program = parts[1]
        ptype = "adult" if parts[2] == "a" else "child"

        group = {
            "program": program,
            "adults": 1 if ptype == "adult" else 0,
            "children": 1 if ptype == "child" else 0,
        }
        context.user_data["groups"].append(group)

        idx = context.user_data.get("person_idx", 0)
        total = context.user_data.get("total", 1)
        context.user_data["person_idx"] = idx + 1

        prog_name = PROGS.get(program, program)
        type_name = "взрослый" if ptype == "adult" else "ребёнок"

        if idx + 1 < total:
            next_num = idx + 2
            await query.edit_message_text(
                f"Человек {idx+1}: {prog_name} — {type_name}\n\n"
                f"Человек {next_num} из {total}. Выберите:",
                reply_markup=person_keyboard()
            )
        else:
            summary = []
            for i, g in enumerate(context.user_data["groups"]):
                p = PROGS.get(g["program"], g["program"])
                t = "ребёнок" if g["children"] > 0 else "взрослый"
                summary.append(f"  {i+1}. {p} — {t}")
            context.user_data["awaiting"] = "days"
            await query.edit_message_text(
                "Все добавлены:\n" + "\n".join(summary) + "\n\nНа сколько дней? (1-7)"
            )
        return

    if data.startswith("order_"):
        await query.answer()
        token = data.replace("order_", "")
        calc_data = context.user_data.get("shared_calc")
        if not calc_data and token:
            calc_data = await api_get(f"/api/share/{token}")
        if not calc_data:
            await query.message.reply_text("Данные устарели. /calc")
            return
        user = query.from_user
        order = await api_post("/api/orders", {
            "menu_id": calc_data.get("menu_id", ""),
            "groups": calc_data.get("groups", []),
            "days": calc_data.get("days", 7),
            "start_day": calc_data.get("start_day", 1),
            "user_id": user.id,
            "user_name": user.username or user.first_name,
            "source": "telegram",
        })
        if order:
            if ADMIN_CHAT_ID:
                try:
                    async with httpx.AsyncClient() as c:
                        names = []
                        for g in calc_data.get("groups", []):
                            p = PROGS.get(g["program"], g["program"])
                            t = "Ребёнок" if g.get("children", 0) > 0 else "Взрослый"
                            names.append(f"{p} ({t})")
                        admin_text = (
                            f"Новый заказ из Telegram!\n\n"
                            f"Пользователь: @{user.username or user.first_name}\n"
                            f"ID: {user.id}\n"
                            f"Рационы: {', '.join(names)}\n"
                            f"Дней: {calc_data.get('days', '?')}\n"
                            f"Сумма: {fmt(calc_data['final_price'])} руб.\n"
                            f"Заказ: #{order['order_id'][:8]}"
                        )
                        await c.post(
                            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                            json={"chat_id": int(ADMIN_CHAT_ID), "text": admin_text},
                            timeout=10
                        )
                except Exception as e:
                    logger.error(f"Failed to notify admin: {e}")
            await query.message.reply_text(
                f"Заказ #{order['order_id'][:8]} создан!\n"
                f"Сумма: {fmt(calc_data['final_price'])} руб.\n\n"
                f"Ожидайте подтверждения!"
            )
        else:
            await query.message.reply_text("Ошибка заказа.")
        return

    await query.answer()


async def show_result(update, context, data):
    lines = []
    for i, g in enumerate(data["groups"]):
        prog = PROGS.get(g["program"], g["program"])
        ptype = "Ребёнок" if g.get("children", 0) > 0 else "Взрослый"
        lines.append(f"  Человек {i+1}: {ptype} — {prog}")
    lines.append(f"Дней: {data['days']}")
    if data.get("discount_percent", 0) > 0:
        lines.append(f"Скидка -{data['discount_percent']}%: -{fmt(data['discount_amount'])} руб.")
    lines.append(f"Итого: {fmt(data['final_price'])} руб.")
    lines.append(f"За человека в день: {fmt(data['per_person_per_day'])} руб.")

    keyboard = [
        [InlineKeyboardButton("Оформить заказ", callback_data=f"order_{data.get('token', '')}")],
    ]

    await update.message.reply_text(
        "Расчёт рационов:\n\n" + "\n".join(lines),
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def do_calc(update, context, groups, days):
    menu = await api_get("/api/latest-menu")
    if not menu:
        await update.message.reply_text("Меню не загружено.")
        return

    body = {
        "menu_id": menu["menu_id"],
        "groups": groups,
        "days": days,
        "start_day": 1,
    }
    logger.info(f"Calc request: {body}")

    result = await api_post("/api/calc", body)
    if not result:
        await update.message.reply_text("Ошибка расчёта.")
        return

    logger.info(f"Calc result: final_price={result.get('final_price')}")
    context.user_data["shared_calc"] = result

    lines = []
    for i, g in enumerate(result["groups"]):
        prog = PROGS.get(g["program"], g["program"])
        ptype = "Ребёнок" if g.get("children", 0) > 0 else "Взрослый"
        lines.append(f"  Человек {i+1}: {ptype} — {prog}")
    lines.append(f"Дней: {result['days']}")
    if result.get("discount_percent", 0) > 0:
        lines.append(f"Скидка -{result['discount_percent']}%: -{fmt(result['discount_amount'])} руб.")
    lines.append(f"Итого: {fmt(result['final_price'])} руб.")
    lines.append(f"За человека в день: {fmt(result['per_person_per_day'])} руб.")

    keyboard = [
        [InlineKeyboardButton("Оформить заказ", callback_data=f"order_{result.get('token', '')}")],
    ]

    await update.message.reply_text(
        "Расчёт рационов:\n\n" + "\n".join(lines),
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


def main():
    if not BOT_TOKEN or BOT_TOKEN == "YOUR_TOKEN_HERE":
        print("Вставьте токен в bot/.env (TELEGRAM_BOT_TOKEN)")
        return

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("calc", calc_start))
    app.add_handler(CommandHandler("orders", my_orders))
    app.add_handler(CommandHandler("site", site_cmd))
    app.add_handler(CallbackQueryHandler(handle_callback))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот Рационика запущен!")
    app.run_polling()


if __name__ == "__main__":
    main()
