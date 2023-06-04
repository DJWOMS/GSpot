#!/bin/bash

set -euo pipefail

python manage.py migrate

gunicorn -b 0.0.0.0:8000 \
--log-level $DJANGO_LOG_LEVEL \
--access-logfile - config.wsgi:application