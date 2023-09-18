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
*Было бы полезно иметь пример с действительными данными для быстрой проверки, а если потребуется, пользователь сможет ввести остальные данные.*


#### Запустить сервер
```
    docker-compose build
    docker-compose up
```
    or
```
    docker-compose up --build
```
*Тут критично важно указывать из какой директории это делать (а может и права указать), в проекте таких файлов несколько!*

**Для запуска отдельных сервисов, нужно по одному, и в правильной очерёдности (?), стартовать `docker-compose up --build` из соответствующих каталогов.**

#### Запустить тесты
```
    docker-compose run web sh -c "python manage.py test"
```

### Создать пользователя
```
    docker-compose run web python manage.py createsuperuser
```

*Тут можно сделать авто-создание superuser, с данными из файла (например .env), тогда для тестовых вариантов будет нужно меньше телодвижений.*

## Известные проблемы
Проект не стартует на некоторых системах линукс с редкими обновлениями - например, LMDE5 (25.04.23).
    
    Причина уточняется, суть проблемы, несовместимость "docker-compose up --build" с ПО из репозиториев.
        packages.linuxmint.com
        deb.debian.org

    Возможное решение, 
        переписать docker-compose для имеющийся версии, 
        или вручную обновлять docker-compose и docker, до необходимой версии... Требования неизвестны!

    Возможный репозиторий для решения...        
```
deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian bullseye stable
```
