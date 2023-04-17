# GSpot - интернет магазин видеоигр

## Мы в сети
- [Telegram](https://t.me/django_school)
- [YouTube](https://www.youtube.com/channel/UC_hPYclmFCIENpMUHpPY8FQ)

## Инструменты

- Python >= 3.9
- Django Rest Framework
- FastAPI
- Docker
- Postgres
- Next.js

### Функционал
#### Для пользователя:


#### Для разработчика:


#### Для владельца сайта:


#### Общий функционал:


## Старт

#### ???В корне проекта переименовать .env.dev-example на .env.dev и прописать свои настройки


#### Запустить сервер

    docker-compose build
    docker-compose up

    or

    docker-compose up --build

#### Запустить тесты

    docker-compose run web sh -c "python manage.py test"

### Создать пользователя

    docker-compose run web python manage.py createsuperuser
