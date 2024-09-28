# Python project initialization
---

### Шаг 1: Инициализация Python-проекта

В Python, аналогом `package.json` является файл `pyproject.toml` или, если использовать старый стандарт, файл `requirements.txt` для зависимостей и виртуального окружения. В последнее время рекомендуется использовать `pyproject.toml`, который позволяет работать с менеджерами зависимостей и сборки, такими как **Poetry** или **Pipenv**.

Я рекомендую использовать **Poetry** для управления зависимостями, поскольку он предоставляет больше возможностей и удобен в работе. Он поддерживает управление версиями, виртуальные окружения и аналогичен функционалу `npm init`.

### Шаг 2: Установка [Poetry](https://python-poetry.org)

[Ссылка](https://pipx.pypa.io/stable/installation/) на инструкцию по установке

### Шаг 3: Инициализация проекта с помощью Poetry

1. Перейдите в директорию проекта или создайте новую:
   ```bash
   mkdir my_python_project && cd my_python_project
   ```

2. Инициализируйте проект:
   ```bash
   poetry init
   ```

   Это запустит интерактивный процесс, где вам будет предложено указать имя проекта, версию Python, необходимые зависимости и т.д.

   **Если хотите автоматизировать инициализацию (аналог `npm init -y`):**
   ```bash
   poetry init --name my_python_project --description "My project" --author "Your Name" --python "^3.10" --dependency flask
   ```

3. После этого в корне проекта будет создан файл `pyproject.toml`, который похож на `package.json`:
   ```toml
   [tool.poetry]
   name = "my_python_project"
   version = "0.1.0"
   description = "My project"
   authors = ["Your Name <your.email@example.com>"]
   python = "^3.10"

   [tool.poetry.dependencies]
   python = "^3.10"
   flask = "^2.0"
   ```

### Шаг 4: Создание виртуального окружения и установка зависимостей

После инициализации проекта, вы можете установить зависимости и создать виртуальное окружение:

1. Создайте виртуальное окружение и установите все зависимости, указанные в `pyproject.toml`:
   ```bash
   poetry install
   ```

   Poetry автоматически создаст виртуальное окружение и установит все зависимости.

2. Активируйте виртуальное окружение:
   ```bash
   poetry shell
   ```

### Шаг 5: Работа с `.env` файлами

Для работы с переменными окружения через `.env` можно использовать библиотеку **python-dotenv**.

1. Добавьте эту библиотеку в зависимости:
   ```bash
   poetry add python-dotenv
   ```

2. Создайте файл `.env` в корне проекта и добавьте туда необходимые переменные окружения. Например:
   ```
   API_KEY=your_api_key
   SECRET_KEY=your_secret_key
   ```

3. В коде вашего приложения, например, в `main.py`, подключите и используйте переменные окружения:
   ```python
   from dotenv import load_dotenv
   import os

   load_dotenv()  # Загружает переменные из .env

   api_key = os.getenv("API_KEY")
   secret_key = os.getenv("SECRET_KEY")

   print(f"API Key: {api_key}, Secret Key: {secret_key}")
   ```

### Шаг 6: Создание Docker-контейнера

Для работы с Docker нужно создать Dockerfile и настроить его для использования вашего проекта.

1. В корне проекта создайте файл `Dockerfile`:
   ```Dockerfile
   # Используем официальный Python образ
   FROM python:3.10-slim

   # Устанавливаем зависимости для системы
   RUN apt-get update && apt-get install -y \
       build-essential

   # Устанавливаем Poetry
   RUN pip install poetry

   # Устанавливаем рабочую директорию
   WORKDIR /app

   # Копируем файлы проекта
   COPY pyproject.toml poetry.lock* /app/

   # Устанавливаем зависимости
   RUN poetry install --no-root

   # Копируем исходный код проекта
   COPY . /app

   # Запуск приложения
   CMD ["poetry", "run", "python", "main.py"]
   ```

2. Включите Docker в своем проекте, чтобы запустить его с теми же переменными окружения. Создайте файл `docker-compose.yml` (для удобного запуска):

   ```yaml
   version: "3.8"
   services:
     app:
       build:
         context: .
         dockerfile: Dockerfile
       environment:
         - API_KEY=${API_KEY}
         - SECRET_KEY=${SECRET_KEY}
       volumes:
         - .:/app
       ports:
         - "8000:8000"
   ```

   Это позволит вам передавать переменные окружения из `.env` в контейнер.

3. Создайте файл `.dockerignore` для исключения ненужных файлов при сборке:
   ```
   __pycache__/
   *.pyc
   .venv
   ```

4. Запустите контейнер:
   ```bash
   docker-compose up --build
   ```

### Шаг 7: Использование зависимостей и версий Python (аналог `engines` в Node.js)

В файле `pyproject.toml` можно задать минимальные требования к версии Python в разделе `[tool.poetry.dependencies]`. Например:
```toml
python = "^3.10"
```

Таким образом, при установке зависимостей Poetry проверит, соответствует ли версия Python установленной в системе.

### Шаг 8: Управление зависимостями

По аналогии с `npm`, можно добавлять или удалять зависимости через Poetry:

1. **Добавление зависимости**:
   ```bash
   poetry add requests
   ```

2. **Удаление зависимости**:
   ```bash
   poetry remove requests
   ```

3. **Обновление всех зависимостей**:
   ```bash
   poetry update
   ```
### Шаг 9: Выбрать Poetry как интерпретатор для VScode
1. **Открыть command pallete** `Command + P`
2. **Ввести команду** `>Python: Select Interpreter`
3. **Выбрать интерпретатор с Poetry**

### Итоговая структура проекта:

```
my_python_project/
│
├── .env                     # Файл с переменными окружения
├── Dockerfile                # Dockerfile для сборки контейнера
├── docker-compose.yml        # Файл для управления сервисами Docker
├── pyproject.toml            # Аналог package.json для зависимостей
├── poetry.lock               # Блокировка версий зависимостей
├── main.py                   # Основной файл приложения
└── .dockerignore             # Исключаем ненужные файлы при сборке Docker
```