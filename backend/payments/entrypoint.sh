#!/usr/bin/env sh
set -o errexit 
set -o nounset

postgres_ready() {
  python << END
import sys

from psycopg2 import connect  
from psycopg2.errors import OperationalError

try:  
  connect(  
        dbname="${POSTGRES_DB}",  
        user="${POSTGRES_USER}",  
        password="${POSTGRES_PASSWORD}",  
        host="${POSTGRES_HOST}",  
        port="${POSTGRES_PORT}",  
    )  
except OperationalError:  
    sys.exit(-1)  
END
}

redis_ready() {
    python << END
import sys
from redis import Redis
from redis import RedisError
try:
    redis = Redis.from_url("${CELERY_BROKER_URL}", db=0)
    redis.ping()
except RedisError:
    sys.exit(-1)
END
}

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py collectstatic --noinput  
python manage.py makemigrations  --noinput 
python manage.py migrate

exec "$@"