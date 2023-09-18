from typing import Type

from base.delivery.base_notify import BaseNotify
from base.models import BaseAbstractUser
from utils.broker.message import NotifyMessage
from utils.broker.rabbitmq import RabbitMQ


class Notify(BaseNotify):
    rabbitmq = RabbitMQ()

    def send_notify(
        self,
        message: NotifyMessage,
    ):
        with self.rabbitmq as rabbit:
            rabbit.send_message(message=message)
