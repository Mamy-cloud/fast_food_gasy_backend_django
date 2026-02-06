#!/usr/bin/env bash
pip install -r requirements.txt
python3 manage.py collectstatic 
python3 manage.py migrate
