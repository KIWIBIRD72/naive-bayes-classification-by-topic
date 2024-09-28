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
CMD ["poetry", "run", "python", "src/__init__.py"]