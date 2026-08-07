# Документация

## Настройка окружения

### Backend (.env)

```
ADMIN_PASSWORD=admin123        # Пароль админ-панели
TELEGRAM_BOT_TOKEN=...         # Токен Telegram-бота
MAX_UPLOAD_SIZE_MB=5           # Макс. размер загружаемого файла
```

### Bot (.env)

```
TELEGRAM_BOT_TOKEN=...         # Токен от @BotFather
API_BASE=http://localhost:8000 # Адрес backend API
ADMIN_PASSWORD=admin123        # Пароль для /upload_menu
```

## Деплой

### Backend

```bash
pip install -r requirements.txt
uvicorn backend.main:app --host 0.0.0.0 --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run build        # соберётся в frontend/dist/
```

Отдайте `frontend/dist/` через nginx или любой статический сервер.

### Bot

Запуск в фоне:
```bash
nohup python bot.py > bot.log 2>&1 &
```

## Где находится меню

Файл меню: `sample_data/sample_menu_ru_headers.xlsx`

Этот файл используется как исходник данных при загрузке через админ-панель или API.

## Пример requests к API

### Загрузка меню

```bash
curl -X POST http://localhost:8000/api/upload-menu \
  -F "file=@sample_data/sample_menu_ru_headers.xlsx"
```

### Расчёт

```bash
curl "http://localhost:8000/api/calc?menu_id=abc123&program=Classic&adults=2&children=0&days=7&start_day=1"
```

Ответ:
```json
{
  "menu_id": "abc123",
  "program": "Classic",
  "adults": 2,
  "children": 0,
  "days": 7,
  "start_day": 1,
  "people_equiv": 2.0,
  "computed_price": 8190.0,
  "kit_price": 6930.0,
  "per_person_per_day": 495.0,
  "currency": "RUB",
  "план": [...]
}
```

### Генерация PDF

```bash
curl -X POST http://localhost:8000/api/generate-pdf \
  -H "Content-Type: application/json" \
  -d '{"menu_id":"abc123","program":"Classic","adults":2,"children":0,"days":7,"start_day":1}' \
  -o report.pdf
```

### Telegram-бот команды

- `/start` — приветствие
- `/calc` — пошаговый расчёт
- `/calc 2 0 7 Classic` — быстрый расчёт (2 взрослых, 0 детей, 7 дней, Classic)
- `/upload_menu` — загрузка .xlsx (только админ)
