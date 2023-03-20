# GSpot Payments

REST API сервис для работы с финансами интернет магазина видеоигр GSpot


## Как запустить local-версию

TODO

## Переменные окружения

Образ Django считывает настройки из переменных окружения:
- `SECRET_KEY` - соль для генерации хэшей. Значение может быть произвольной строкой
- `DEBUG`- настройка Django для ключения отладочного режима.
- `ALLOWED_HOSTS` - список разрешенных хостов.
- `DATABASE_URL` - адрес для подключения к БД PostgreSQL. [Формат записи](https://github.com/jacobian/dj-database-url#url-schema)
- `account_id` - id вашего магазина yookassa.
- `shop_secret_key` - api ключ вашего магазина yookassa.

## Установка и настройка flake8
На проекте используется линтер flake8 с плагинами. Flake8 не дает возможности перечислить используемые плагины,
поэтому если у вас есть другие проекты с flake8, то их плагины начнут мешать друг другу. Чтобы избежать этого
необходимо создать отдельное виртуальное окружение под линтер.

Устанавливаем flake8 и плагины для него:
```shell
virtualenv venv
source ../venv/bin/activate
pip install -r flake8-requirements.txt
```

Настройте IDE для использования flake8 из виртуального окружения (не из глобального):
- Pycharm - [статья 1](https://melevir.medium.com/pycharm-loves-flake-671c7fac4f52), [статья 2](https://habr.com/en/company/dataart/blog/318776/);
- [Vscode](https://stackoverflow.com/questions/54160207/using-flake8-in-vscode/54160321#54160321).

### Насторойка flake8 для запуска проверки в pre-commit hooks

Установить pre-commit:
```shell
pre-commit install
```

В последующем все проиндексированные файлы будут проверяться с помощью flake8 перед коммитом.

Для проверки с помощью flake8 файлов проиндексированных для коммита выполнить:
```shell
pre-commit run  
```
В случае необходимости пропустить использование pre-commit hook коммит нужно выполнить с флагом `-n` или `--no-verify`:
```shell
git commit --no-verify
```
Для автоматического обновления версии hooks, используемых в pre-commit выполнить:
```shell
pre-commit autoupdate
```

### Запуск Docker  контейнера

Создания образа:
$ docker-compose build
 
Запуск нескольких контейнеров одновременно:
$ docker-compose up

Две предыдущие команды можно обьединить в одну:
$ docker-compose up --build -d
    -d: запустит контейнеры в фоновом режиме

Остановка всех запущенных контейнеров:
$ docker-compose down

Удаление всех остановленных контейнеров:
$ docker container prune

Миграция БД:
$ docker-compose exec web python manage.py makemigrations
$ docker-compose exec web python manage.py migrate

Работа с контейнерами:
$ docker ps                            ## показывает список запущенных контейнеров
$ docker ps -a                         ## показывает список запущенных и остановленных контейнеров
$ docker restart <Container ID>        ## перезапускает контейнер
$ docker stop <Container ID>           ## останавливает контейнер
$ docker rmi <Container ID>            ## удаляет контейнер
$ docker exec -it <Container ID> bash  ## запускает интерактивный терминал с оболочкой bash  внутри контейнера