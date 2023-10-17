FROM python:3.9-slim-buster

#WORK DIR

WORKDIR /app


#Установите переменные окружения для предотвращения
#вывода сообщений Python в stdout

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app/

RUN pip install gunicorn

CMD ["gunicorn", "--bind", "0.0.0.0:9900", "/home/alexa/python_mor/django_rest/EventOrganization:app"]

RUN pip install --upgrade pip \
      && pip install -r requirements.txt

# Копируем содержимое текущей директории в контейнер

COPY . /app/

