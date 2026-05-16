### Задания

[Задание 9](app/Images.md)

[Задание 10](Task10/tasks.md)

[Задание 11](Task11/tasks.md)

---

## Настройка и запуск проекта

### 1. Клонирование репозитория

```bash
git clone https://github.com/hsugvusrihgvir/uni-tdsa-4-kr4
cd uni-tdsa-4-kr4
```

### 2. Создание виртуального окружения

```bash
python -m venv .venv
```

### 3. Активация виртуального окружения

Для Windows:

```bash
.venv\Scripts\activate
```

Для Linux/macOS:

```bash
source .venv/bin/activate
```

### 4. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 5. Переменные окружения

Пример:

[.env.example](.env.example)

На его основе создать локальный файл `.env`.


---

## Запуск приложения

Для запуска FastAPI-приложения перейдите в нужную папку задания и выполните команду:

```bash
uvicorn main:app --reload
```

Например, для задания 10:

```bash
cd Task10
uvicorn main:app --reload
```

После запуска приложение будет доступно по адресу:

```text
http://127.0.0.1:8000
```

Документация Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## Проверка основной функциональности

### Задание 9

Применить миграции:

```bash
alembic upgrade head
```

Создать новую миграцию после изменения модели:

```bash
alembic revision --autogenerate -m "add product description"
```


### Задание 10

Пример запуска:

```bash
cd Task10
uvicorn main:app --reload
```

Проверить эндпоинты можно через Swagger UI:

```text
http://127.0.0.1:8000/docs
```

Также можно отправить POST-запрос с корректными и некорректными данными, чтобы проверить обработку ошибок валидации.

### Задание 11


Запуск тестов:

```bash
cd Task11
pytest
```

