#!/bin/bash

set -o errexit  
set -o pipefail  
set -o nounset

# postgres_ready() {  
#     python -<<END  
# import sys

# from psycopg2 import connect  
# from psycopg2.errors import OperationalError

# try:  
#     connect(  
#         dbname="${POSTGRES_DB}",  
#         user="${POSTGRES_USER}",  
#         password="${POSTGRES_PASSWORD}",  
#         host="${POSTGRES_HOST}",  
#         port="${POSTGRES_PORT}",  
#     )  
# except OperationalError:  
#     sys.exit(-1)  
# END  
# }

# until postgres_ready; do  
#   >&2 echo "Waiting for PostgreSQL to become available..."  
#   sleep 5  
# done  
# >&2 echo "PostgreSQL is available"

python manage.py collectstatic --noinput  
python manage.py makemigrations  --noinput 
python manage.py migrate

exec "$@"
