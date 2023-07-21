from . import rabbitmq

CELERY_BROKER_URL = (
    f"amqp://{rabbitmq.RABBITMQ_USERNAME}:{rabbitmq.RABBITMQ_PASSWORD}@"
    f"{rabbitmq.RABBITMQ_HOST}:{rabbitmq.RABBITMQ_PORT}{rabbitmq.RABBITMQ_VIRTUAL_HOST}"
)

CELERY_TASK_DEFAULT_QUEUE = "users_queue"

CELERY_TASK_DEFAULT_EXCHANGE = "users_exchange"
