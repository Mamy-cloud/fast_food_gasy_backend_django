#!/usr/bin/env bash
pip install -r requirements.txt
python manage.py collectstatic --noinput
python makemigrations
python manage.py migrate
