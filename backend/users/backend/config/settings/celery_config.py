from config.settings import rabbitmq

CELERY_BROKER_URL = (
    f"amqp://{rabbitmq.RABBITMQ_USERNAME}:{rabbitmq.RABBITMQ_PASSWORD}@"
    f"{rabbitmq.RABBITMQ_HOST}:{rabbitmq.RABBITMQ_PORT}{rabbitmq.RABBITMQ_VIRTUAL_HOST}"
)
