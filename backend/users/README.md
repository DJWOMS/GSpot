# GSpot users service

## Quick Start

**NOTE**: The project uses Python 3.11, so need it installed first. It is recommended to use [`Poetry`](https://github.com/python-poetry/poetry) for installation.

**NOTE**: Root of the django project is at the `backend` folder

Here is a short instruction on how to quickly set up the project for development:

## Poetry guide

**NOTE**: Run commands in directory with `pyproject.toml`

**NOTE**: Check for Poetry exist in $PATH

### Installing dependencies:
- All dependencies (recommended)
```
$ poetry install
```
- Without development dependencies
```
$ poetry install --without dev
```
### Running shell (Poetry auto-generated virtual environment):
```
$ poetry shell
```
[`More commands`](https://python-poetry.org/docs/cli/)
            
## Before start

- Check environment variables in `.env.prod` for production environment or `.env.tests` for running tests
    
### Environment variables
#### Django:

- `DEBUG` - variable for defining environment for project `(True/False)`
- `DJANGO_LOG_LEVEL` - variable for defining level of logger 
  - Possible values:
  - <i style="color:#00c8ff">DEBUG</i>: Low level system information for debugging purposes
  - <i style="color:#00c8ff">INFO</i>: General system information
  - <i style="color:#00c8ff">WARNING</i>: Information describing a minor problem that has occurred.
  - <i style="color:#00c8ff">ERROR</i>: Information describing a major problem that has occurred.
  - <i style="color:#00c8ff">CRITICAL</i>: Information describing a critical problem that has occurred.
- `DJANGO_SECRET_KEY` - secret key of django project, generates via
```
$ python manage.py shell
>>> from django.core.management.utils import get_random_secret_key
>>> get_random_secret_key()
```
- `DJANGO_CORS_ALLOWED_ORIGINS` - sources that can make requests to django API (default `http://localhost:3000`)
- `DJANGO_ALLOWED_HOSTS` - hosts that django can run on in production (default `*`)
- `GET_TOKEN_FROM` - where to get JWT tokens `(headers/cookies)`

#### Django superuser credentials:

- `DJANGO_SUPERUSER_USERNAME` - superuser's usersname
- `DJANGO_SUPERUSER_PHONE` - superuser's phone
- `DJANGO_SUPERUSER_EMAIL` - superuser's email
- `DJANGO_SUPERUSER_PASSWORD` - superuser's password

#### PostgreSQL:

- `POSTGRES_DB` - database name
- `POSTGRES_USER` - database owner
- `POSTGRES_PASSWORD` - database password
- `POSTGRES_HOST` - host on which the database runs
- `POSTGRES_PORT` - port on which the database runs

#### RabbitMQ:

- `RABBITMQ_HOST` - host on which RabbitMQ runs
- `RABBITMQ_PORT` - port on which RabbitMQ runs
- `RABBITMQ_USERNAME` - username of RabbitMQ panel account
- `RABBITMQ_PASSWORD` - password of RabbitMQ panel account
- `RABBITMQ_VIRTUAL_HOST` - relative path on RabbitMQ host from application

#### JWT Tokens:

- `ACCESS_TOKEN_LIFETIME` - time until access token expires (in sec.)
- `REFRESH_TOKEN_LIFETIME` - time until refresh token expires (in sec.)

## Run through docker-compose for development


**NOTE**: docker-compose.yml - for project   
**NOTE**: docker-compose.tests.yml - for running project's tests

### To start project run
```
$ docker-compose -f docker-compose.yml up -d --build
                                           |     |
                                           |     |
                      in detach mode ______|     |______ for image rebuilding
```
### To run project's tests
```
$ docker-compose -f docker-compose.tests.yml \
                 up \
                 --build  \
                 --abort-on-container-exit \
                 --exit-code-from  web_users_tests

```
## Execute commands in docker

In order to run command in container use:
```
$ docker-compose exec {container_name} \
                      {command}
```
Example:
```
$ docker-compose exec web_users \
      python manage.py makemigrations
```

### Create superuser
```
$ docker-compose exec web_users \
      python manage.py createsuperuser
```

### Create permission for Admin and Developer
To create permissions quickly you can use 
#### For Admin
```
$ docker-compose exec web_users \
      python manage.py createadminpermission  \
      name=test \
      codename=testcode
```
#### For Developer
```
$ docker-compose exec web_users \
      python manage.py createdeveloperpermission  \
      name=test \
      codename=testcode
```
