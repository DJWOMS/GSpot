#!/usr/bin/env sh
set -o errexit 
set -o nounset


python manage.py collectstatic --noinput  
python manage.py migrate
python manage.py apps/base/fixtures/base/*.json
gunicorn config.wsgi:application --bind :8000 -k gevent

exec "$@"