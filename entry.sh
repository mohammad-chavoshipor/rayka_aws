#!/bin/sh
sleep 10

alias python=python3
python manage.py makemigrations
python manage.py migrate

# runs the server
python manage.py runserver 0.0.0.0:8000
