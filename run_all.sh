#!/bin/bash

source /app/iury/bin/activate
python manage.py makemigrations && python manage.py migrate
gunicorn --reload uea_news.wsgi -b 0.0.0.0:9000 &  # Execute em segundo plano
python media_watcher.py