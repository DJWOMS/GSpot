import pika
from django.conf import settings
from utils.broker.rabbitmq import RabbitMQ


class TearDown:
    def tearDown(self) -> None:
        self.rabbitmq = RabbitMQ()
        with self.rabbitmq:
            try:
                self.rabbitmq._channel.queue_purge(queue=settings.EMAIL_ROUTING_KEY)
                self.rabbitmq._channel.queue_purge(queue=settings.NOTIFY_ROUTING_KEY)
            except pika.exceptions.ChannelClosedByBroker:
                pass
