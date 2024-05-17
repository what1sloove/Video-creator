# Используем официальный Python образ в качестве базового
FROM python:3.12

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей и устанавливаем зависимости
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Копируем весь проект в контейнер
COPY . /app/

# Открываем порт, который будет использован
EXPOSE 8000

# Запускаем приложение
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
