# GSpot Payments

REST API service for working with finance online video game store GSpot.

## Environment variables

Django image reads settings from environment variables, default settings for test run in `.env.example`:
- `SECRET_KEY` - salt for hash generation. The value can be an arbitrary string.
- `DEBUG` - configuring Django to enable debug mode.
- `ALLOWED_HOSTS` - list of allowed hosts.
- `SHOP_ACOUNT_ID` - id of your [yookassa](https://yookassa.ru/yooid/signin/step/login?origin=Checkout&returnUrl=https%3A%2F%2Fyookassa.ru%2Fmy%3Fget-auth%3Dyes) store.
- `SHOP_SECRET_KEY` - api key of your [yookassa](https://yookassa.ru/yooid/signin/step/login?origin=Checkout&returnUrl=https%3A%2F%2Fyookassa.ru%2Fmy%3Fget-auth%3Dyes) store.
- `ROLLBAR_ACCESS_TOKEN` - token [rollbar](https://rollbar.com/) for logging events.
- `POSTGRES_DB` - db of postgres.
- `POSTGRES_USER` - user for postgres.
- `POSTGRES_PASSWORD` - password for postgres.
- `POSTGRES_PORT` - port for postgres.
- `POSTGRES_HOST` - host for postgres, if local - localhost, if docker - name of container.
- `REDIS` - broker for celery, variable in **settings.py -> CELERY_BROKER_URL**.
- `SUBDOMAIN` - for localtunnel, use it for yookassa.

## How to run local-version

>Firstly, I recommend to run project by Docker, it's much easier but if you want local, you can.

1. Create virtual environment and activate them:

```shell
python -m venv venv             ## windows
./venv/scripts/activavte        ## windows

virtualenv venv                 ## linux
source ../venv/bin/activate     ## linux
```

2. Install requirements:

```shell
pip install -r requirements.txt
```

3. If you want to make commit, you also need to install `Flake8` requirements and `pre-commit`, desription below.

4. Set your `.env` file, also you can use `.env.example`.

5. Make migrations and run server.

```shell
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

6. At now, we have two main endpoints to work with payments.

- `/api/v1/payment_accounts/create_payment/` - for create payments.
- `/api/v1/payment_accounts/payment_acceptance/` - for confirm payments from yookassa.
 
## Flake 8 installation and setup
The project uses `Flake8` linter with plugins. `Flake8` does not allow you to list the plugins used, so if you have other projects with `Flake8`, their plugins will start to interfere with each other. To avoid this you must create a separate virtual environment for the linter.

Install `Flake8` and plugins for him:
```shell
pip install -r flake8-requirements.txt
```

Configure the IDE to use `Flake8` from the virtual environment (not the global):
- Pycharm - [first article](https://melevir.medium.com/pycharm-loves-flake-671c7fac4f52), [second article](https://habr.com/en/company/dataart/blog/318776/);
- [VS Code](https://stackoverflow.com/questions/54160207/using-flake8-in-vscode/54160321#54160321).

### Configure Flake8 to run check in pre-commit hooks

Install `pre-commit`:
```shell
pre-commit install
```

Subsequently, all indexed files will be checked with `Flake8` before committing.

To check with `Flake8` the files indexed for the commit run:
```shell
pre-commit run  
```
If it's necessary to skip using `pre-commit hook`, the commit should run with the `-n` or `--no-verify` flag:
```shell
git commit --no-verify
```
To automatically update the version of the `pre-commit hook` run:
```shell
pre-commit autoupdate
```

## Run Docker container

Creating an image:
```shell
$ docker-compose build
```

Running multiple containers at the same time:
```shell
$ docker-compose up
```

The two previous commands can be combined into one, `-d` runs container in the background:
```shell
$ docker-compose up --build -d
```

Stop all running containers:
```shell
$ docker-compose down
```

Deleting all stopped containers:
```shell
$ docker container prune
```

Migrate DB:
```shell
$ docker-compose exec web python manage.py makemigrations
$ docker-compose exec web python manage.py migrate
```

Working with containers:
```shell
$ docker ps                            ## list of running containers
$ docker ps -a                         ## list of running and stopped containers
$ docker restart <Container ID>        ## restart container
$ docker stop <Container ID>           ## stop container
$ docker rmi <Container ID>            ## delete container
$ docker exec -it <Container ID> bash  ## run an interactive terminal with bash inside container
```

## Yookassa

1. Firstly, you need to registrate on [Yookassa](https://yookassa.ru/yooid/signin/step/login?origin=Checkout&returnUrl=https%3A%2F%2Fyookassa.ru%2Fmy%3Fget-auth%3Dyes) and create test shop. Also you can see your **shop id** here.

![alt text](https://i.pinimg.com/originals/2d/97/6c/2d976cf481d6e905136ee8214fcf0f9c.jpg)

2. Next step you need to get **api key**.

![alt text](https://i.pinimg.com/originals/d2/d7/53/d2d753a6a63e375bb7acff6c0631e3d2.jpg)

3. Set your **api key** and **shop id** in `.env` file.

4. After command `docker-compose up` node container gives you link, like this:

```shell
$ payments-node-1 | your url is: https://yoursubdomain.loca.lt
```

Or if you start project local you need to use [`ngrok`](https://ngrok.com/) or node module [`localtunnel`](https://www.npmjs.com/package/localtunnel) for it.

5. At last, you need to put this link in yookassa settings and you're done:

![alt text](https://i.pinimg.com/originals/90/1a/27/901a279e9df3b0da2bcac4f236fc3a4b.png)
-