import pika

from config.settings.rabbitmq import RABBITMQ_HOST, RABBITMQ_PORT, RABBITMQ_USERNAME, RABBITMQ_PASSWORD
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
            virtual_host='/',
            credentials=credentials
        )
        self._connection = pika.BlockingConnection(parameters)
        self._channel = self._connection.channel()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._connection.close()

    def send_message(self, message: BaseMessage) -> None:
        self._channel.basic_publish(
            exchange=message.exchange_name,
            routing_key=message.routing_key,
            body=message.to_bytes()
        )
