from .settings import settings

RABBIT_URL = f'amqp://{settings.RABBITMQ_DEFAULT_USER}:{settings.RABBITMQ_DEFAULT_PASS}@{settings.RABBITMQ_LOCAL_HOST_NAME}:{settings.RABBITMQ_LOCAL_PORT}/'
