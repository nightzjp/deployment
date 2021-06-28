#!/bin/bash

#pipenv run python manage.py migrate
#pipenv run python manage.py runserver 0.0.0.0:8000


if [ $1 ]; then
  if [ $1 = 'celery' ]; then
    pipenv run python manage.py makemigrations
    pipenv run python manage.py migrate
    pipenv run celery -A deployment worker -B -l info
  else
    pipenv run python manage.py makemigrations
    pipenv run python manage.py migrate
    pipenv run python manage.py $1
  fi
else
  echo "default"
  pipenv run python manage.py makemigrations
  pipenv run python manage.py migrate
  export DJANGO_SUPERUSER_PASSWORD=root!@#$%
  pipenv run python manage.py createsuperuser --noinput --username Root  --email Root@localhost.com
  pipenv run python manage.py runserver 0.0.0.0:8888
fi
