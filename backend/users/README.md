# GSpot users service

## Quick Start

**NOTE**: The project uses Python 3.11, so need it installed first. It is recommended to use [`pyenv`](https://github.com/pyenv/pyenv) for installation.

**NOTE**: Root of the django project is at the `backend` folder

Here is a short instruction on how to quickly set up the project for development:

1. Install [`poetry`](https://python-poetry.org/)
2. `git clone https://github.com/DJWOMS/GSpot.git`
3. `cd gspot/backend/users`
4. Install requierements:

```bash
$ poetry install
$ poetry shell
```

5. Install pre-commit hooks: `$ pre-commit install`
6. Initiate the database: `$ cd backend && poetry run python manage.py migrate`
7. Add and setup .env file: `$ cp .env.example .env` -> edit `.env`
8. Manually create a superuser: `$ python manage.py createsuperuser --username admin --email admin@admin.com`
9. Run the server: `$ poetry run python manage.py runserver`

### Use with Docker

For local development (from `gspot/users/ directory`):

`$ docker-compose -f docker/docker-compose.yml -f docker/docker-compose.local.yml --env-file ./.env up -d --build`

Read more [here](https://docs.docker.com/compose/extends/)

### Use Postgres with Docker

The project used Postgres as db engine. To use postgres with docker:

1. Add `POSTGRES_DB=gspot_users, POSTGRES_USER=postgres, POSTGRES_PASSWORD=postgres` to `.env`
2. From project root run `$ docker run --rm --volume pgdata:/var/lib/postgresql/data --name pg --env-file ./.env -d -p 5432:5432 postgres:14-alpine`
