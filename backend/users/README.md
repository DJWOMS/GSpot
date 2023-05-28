# GSpot users service

## Quick Start

**NOTE**: The project uses Python 3.11, so need it installed first. It is recommended to use [`pyenv`](https://github.com/pyenv/pyenv) for installation.

**NOTE**: Root of the django project is at the `backend` folder

Here is a short instruction on how to quickly set up the project for development:

## Run through docker-compose


**NOTE**: docker-compose.yml - for project   
**NOTE**: docker-compose.local.yml - for project's db (Postgres, Redis, Rabbitmq)  
**NOTE**: docker-compose.tests.yml - for running project's tests
            

### To start project locally run
```
$ docker-compose -f docker-compose.yml \
                 -f docker-compose.local.yml \
                 up \
                 --build 
```
### To run project's tests
```
$ docker-compose -f docker-compose.tests.yml \
                 -f docker-compose.local.yml \
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

