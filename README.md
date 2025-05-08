# User CRUD API

REST API для управления пользователями, построенный с использованием LiteStar и PostgreSQL.

## Технологии

- Python 3.12
- LiteStar 2.x
- PostgreSQL
- Docker
- Poetry 1.8.3
- Advanced-SQLAlchemy
- msgspec

## Инструкция по запуску

1. Клонировать репозиторий:
```bash
git clone [ваша_ссылка]
cd user_crud_test
```

2. Запустить приложение:
```bash
docker-compose up -d
```

## API Endpoints

API доступен по адресу: http://localhost:8000

Swagger документация: http://localhost:8000/schema/swagger

### Доступные эндпоинты:

- `POST /users` - Создание пользователя
- `GET /users` - Получение списка пользователей
- `GET /users/{id}` - Получение данных конкретного пользователя
- `PUT /users/{id}` - Обновление данных пользователя
- `DELETE /users/{id}` - Удаление пользователя

## Примеры запросов

### Создание пользователя
```bash
curl -X POST http://localhost:8000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "John", "surname": "Doe", "password": "secret123"}'
```

### Получение списка пользователей
```bash
curl http://localhost:8000/users
```

### Получение конкретного пользователя
```bash
curl http://localhost:8000/users/1
```

### Обновление пользователя
```bash
curl -X PUT http://localhost:8000/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "John", "surname": "Smith", "password": "newpass123"}'
```

### Удаление пользователя
```bash
curl -X DELETE http://localhost:8000/users/1
```

## Время реализации

[Укажите время, потраченное на реализацию]
