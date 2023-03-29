#!/usr/bin/env sh

cd $APP_HOME

if [ $# -eq 0 ]; then
    echo "Usage: start.sh [PROCESS_TYPE](server)"
    exit 1
fi

PROCESS_TYPE=$1

if [ "$PROCESS_TYPE" = "server" ]; then
    if [ "$DEBUG" = "1" ]; then
        python manage.py runserver 0.0.0.0:8000
    fi

fi