FROM python:3.9-slim-buster

#WORK DIR

WORKDIR /app


#Установите переменные окружения для предотвращения
#вывода сообщений Python в stdout

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app/

RUN pip install gunicorn


RUN pip install --upgrade pip \
      && pip install -r requirements.txt

# Копируем содержимое текущей директории в контейнер

COPY . /app/
