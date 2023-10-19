#!/bin/sh

until cd /app/
do
    echo 'Waiting for server volume...'
done
until ./manage.py migrate
do
    echo 'Waiting for db to be ready...'
    sleep 2
done

./manage.py collectstatic --no-input
./manage.py makemigrations && ./manage.py migrate

gunicorn EventOrganization.wsgi --bind 0.0.0.0:9000 --workers 4 --threads 4