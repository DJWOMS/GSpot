import pika
from config.settings.rabbitmq import (
    RABBITMQ_HOST,
    RABBITMQ_PASSWORD,
    RABBITMQ_PORT,
    RABBITMQ_USERNAME,
)
from utils.broker.message import BaseMessage


class RabbitMQ:
    def __init__(self):
        self.host = RABBITMQ_HOST
        self.port = RABBITMQ_PORT
        self.username = RABBITMQ_USERNAME
        self.password = RABBITMQ_PASSWORD
        self._connection = None
        self._channel = None

    def __enter__(self):
        credentials = pika.PlainCredentials(self.username, self.password)
        parameters = pika.ConnectionParameters(
            host=self.host,
            port=self.port,
            virtual_host="/",
            credentials=credentials,
        )
        self._connection = pika.BlockingConnection(parameters)
        self._channel = self._connection.channel()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._connection.close()

    def send_message(self, message: BaseMessage) -> None:
        self.declare_exchange_and_queue(message.exchange_name, message.routing_key)
        self._channel.basic_publish(
            exchange=message.exchange_name,
            routing_key=message.routing_key,
            body=message.to_bytes(),
        )

    def declare_exchange_and_queue(self, exchange_name: str, routing_key: str):
        self._channel.exchange_declare(exchange=exchange_name, exchange_type="direct")
        self._channel.queue_declare(queue=routing_key)
        self._channel.queue_bind(exchange=exchange_name, queue=routing_key, routing_key=routing_key)
