import os
import logging
from dotenv import load_dotenv
import httpx
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, MessageHandler, ConversationHandler,
    CallbackQueryHandler, filters, ContextTypes
)

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
API_BASE = os.getenv("API_BASE", "http://localhost:8000")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin123")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

MENU_ID = None
PROGRAM, ADULTS, CHILDREN, DAYS, START_DAY = range(5)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я бот-калькулятор рационов.\n\n"
        "Доступные команды:\n"
        "/calc — расчёт пошагово\n"
        "/calc A C D Program — быстрый расчёт\n"
        "  A = взрослые, C = дети, D = дни\n"
        "  Program = Classic | Balance | Vegan\n"
        "  Пример: /calc 2 0 7 Classic"
    )


async def calc_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.replace("/calc", "").strip()
    if text:
        return await quick_calc(update, context, text)

    await update.message.reply_text(
        "Выберите программу:",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Classic", callback_data="prog_Classic"),
             InlineKeyboardButton("Balance", callback_data="prog_Balance"),
             InlineKeyboardButton("Vegan", callback_data="prog_Vegan")]
        ])
    )
    return PROGRAM


async def quick_calc(update: Update, context: ContextTypes.DEFAULT_TYPE, text: str):
    global MENU_ID
    parts = text.split()
    if len(parts) != 4:
        await update.message.reply_text("Формат: /calc A C D Program\nПример: /calc 2 0 7 Classic")
        return ConversationHandler.END

    try:
        adults, children, days = int(parts[0]), int(parts[1]), int(parts[2])
        program = parts[3]
    except ValueError:
        await update.message.reply_text("Ошибка в параметрах. Используйте: /calc 2 0 7 Classic")
        return ConversationHandler.END

    if not MENU_ID:
        await update.message.reply_text("Меню не загружено. Используйте /upload_menu (только для админа).")
        return ConversationHandler.END

    await do_calc(update, context, program, adults, children, days, 1)


async def program_selected(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    context.user_data['program'] = query.data.replace("prog_", "")
    await query.edit_message_text(f"Программа: {context.user_data['program']}\nСколько взрослых?")
    return ADULTS


async def adults_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        context.user_data['adults'] = max(1, int(update.message.text))
    except ValueError:
        await update.message.reply_text("Введите число:")
        return ADULTS
    await update.message.reply_text("Сколько детей?")
    return CHILDREN


async def children_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        context.user_data['children'] = max(0, int(update.message.text))
    except ValueError:
        await update.message.reply_text("Введите число:")
        return CHILDREN
    await update.message.reply_text("На сколько дней? (1-7)")
    return DAYS


async def days_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        context.user_data['days'] = max(1, min(7, int(update.message.text)))
    except ValueError:
        await update.message.reply_text("Введите число 1-7:")
        return DAYS

    await do_calc(
        update, context,
        context.user_data['program'],
        context.user_data['adults'],
        context.user_data['children'],
        context.user_data['days'],
        1
    )
    return ConversationHandler.END


async def do_calc(update, context, program, adults, children, days, start_day):
    global MENU_ID
    if not MENU_ID:
        await update.message.reply_text("Меню не загружено.")
        return

    params = {
        "menu_id": MENU_ID,
        "program": program,
        "adults": adults,
        "children": children,
        "days": days,
        "start_day": start_day,
    }

    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(f"{API_BASE}/api/calc", params=params, timeout=30)
            if resp.status_code != 200:
                await update.message.reply_text(f"Ошибка: {resp.text}")
                return
            data = resp.json()
    except Exception as e:
        await update.message.reply_text(f"Ошибка соединения: {e}")
        return

    fmt = lambda v: f"{round(v):,}".replace(",", " ")

    g = data['groups'][0]
    text = (
        f"Расчёт: {g['program']}\n"
        f"Взрослые: {g['adults']} | Дети: {g['children']}\n"
        f"Дней: {data['days']} | Эквивалент: {g['people_equiv']} чел.\n\n"
        f"Стоимость по тарифу: {fmt(data['total_kit_price'])} {data['currency']}\n"
        f"Расчётная: {fmt(data['total_computed_price'])} {data['currency']}\n"
        f"За человека в день: {fmt(data['per_person_per_day'])} {data['currency']}\n\n"
        f"План по дням:\n"
    )

    for day in g['plan']:
        text += f"\nДень {day['День']} ({fmt(day['дневная_стоимость'])} {data['currency']}):\n"
        for meal in day['приёмы']:
            text += f"  {meal['Приём']}:\n"
            for b in meal['блюда']:
                text += f"    - {b['Название_блюда']} ({fmt(b['Стоимость_строки'])} {data['currency']})\n"

    keyboard = []
    if data.get('token'):
        keyboard.append([
            InlineKeyboardButton("Подробнее", url=f"{API_BASE.replace('localhost', '127.0.0.1')}#/result/{data['token']}")
        ])

    await update.message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard) if keyboard else None
    )


async def upload_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global MENU_ID
    if not update.message.document:
        await update.message.reply_text("Отправьте файл .xlsx")
        return

    file = await context.bot.get_file(update.message.document.file_id)
    tmp_path = "/tmp/menu_upload.xlsx"
    await file.download_to_drive(tmp_path)

    try:
        import httpx
        with open(tmp_path, "rb") as f:
            resp = httpx.post(
                f"{API_BASE}/api/upload-menu",
                files={"file": ("menu.xlsx", f, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")},
                timeout=30,
            )
        data = resp.json()

        if data.get("errors"):
            await update.message.reply_text(
                f"Ошибки при загрузке:\n" + "\n".join(e["message"] for e in data["errors"])
            )
        else:
            MENU_ID = data["menu_id"]
            await update.message.reply_text(f"Меню загружено: {data['row_count']} строк, ID: {MENU_ID}")
    except Exception as e:
        await update.message.reply_text(f"Ошибка загрузки: {e}")


def main():
    if not BOT_TOKEN:
        print("Ошибка: TELEGRAM_BOT_TOKEN не задан в .env")
        return

    app = Application.builder().token(BOT_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("calc", calc_start)],
        states={
            PROGRAM: [CallbackQueryHandler(program_selected, pattern="^prog_")],
            ADULTS: [MessageHandler(filters.TEXT & ~filters.COMMAND, adults_input)],
            CHILDREN: [MessageHandler(filters.TEXT & ~filters.COMMAND, children_input)],
            DAYS: [MessageHandler(filters.TEXT & ~filters.COMMAND, days_input)],
        },
        fallbacks=[CommandHandler("start", start)],
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(conv_handler)
    app.add_handler(CommandHandler("upload_menu", upload_menu))

    print("Бот запущен...")
    app.run_polling()


if __name__ == "__main__":
    main()
