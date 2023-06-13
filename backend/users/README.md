# GSpot users service

## Quick Start

**NOTE**: The project uses Python 3.11, so need it installed first. It is recommended to use [`pyenv`](https://github.com/pyenv/pyenv) for installation.

**NOTE**: Root of the django project is at the `backend` folder

Here is a short instruction on how to quickly set up the project for development:

            
## Before start

- Check environment variables in .env.example
    
### Environment variables

- `DJANGO_ENV` - variable for defining environment for project (DEVELOPMENT/PRODUCTION)
- `DJANGO_LOG_LEVEL` - variable for defining level of logger 
  - Possible values:
  - DEBUG: Low level system information for debugging purposes
  - INFO: General system information
  - WARNING: Information describing a minor problem that has occurred.
  - ERROR: Information describing a major problem that has occurred.
  - CRITICAL: Information describing a critical problem that has occurred.
    
- `DJANGO_CORS_ALLOWED_ORIGINS` - http://localhost:8080, http://localhost:8000
- `DJANGO_ALLOWED_HOSTS` - http://localhost:8080, http://localhost:8000

## Run through docker-compose for development


**NOTE**: docker-compose.yml - for project   
**NOTE**: docker-compose.tests.yml - for running project's tests

### To start project run
```
$ docker-compose -f docker-compose.yml up --build 
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

