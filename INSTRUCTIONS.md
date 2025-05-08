# Инструкция по установке и запуску

## Ссылка на GitHub
https://github.com/XRU13/user_crud_lightstar.git

## Шаги установки

1. Клонировать репозиторий:
```bash
git clone https://github.com/XRU13/user_crud_lightstar.git
cd user_crud_lightstar
```

2. Запустить приложение (выберите один из способов):

   a. Через Docker Compose:
   ```bash
   docker compose up -d
   ```

   b. Через uvicorn:
   ```bash
   uvicorn app.asgi:app --host 127.0.0.1 --port 8000
   ```

3. Применить миграции:
```bash
litestar database upgrade
```

## Время реализации
Примерно 5 часов, включая:
- Настройку проекта и структуры
- Реализацию CRUD операций
- Настройку Docker и миграций
- Подключени линтеров
- Документирование 