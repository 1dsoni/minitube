#!/usr/bin/env bash
# to perform all the steps for running the project in a docker

./wait-for-it.sh -t 300 "${DB_HOST}":"${DB_PORT}" -- echo db is up

python3.8 manage.py migrate

gunicorn --bind :8000 --workers 4 wsgi:application
