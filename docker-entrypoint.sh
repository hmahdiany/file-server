#!/bin/sh

# Collect static files
echo "Collect static files"
python manage.py collectstatic

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Start server
echo "Starting server"
gunicorn --bind :8000 --workers 3 fileServer.wsgi:application