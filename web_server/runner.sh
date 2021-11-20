#!/usr/bin/env bash
# to perform all the steps for running the project in a docker

./manage.py migrate

gunicorn --bind :8000 --workers 4 wsgi:application
