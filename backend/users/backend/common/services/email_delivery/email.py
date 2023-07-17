from typing import Type

from base.delivery.base_email import BaseEmail
from base.delivery.base_notify import BaseNotify
from base.models import BaseAbstractUser
from utils.broker.message import (
    AdminActivationMessage,
    CustomerActivationMessage,
    DevelopActivationMessage,
    NotifyMessage,
)
from utils.broker.rabbitmq import RabbitMQ


class EmailDelivery(BaseEmail):
    rabbitmq = RabbitMQ()

    def send_email(
        self,
        message: AdminActivationMessage | CustomerActivationMessage | DevelopActivationMessage,
    ):
        with self.rabbitmq as rabbit:
            rabbit.send_message(message=message)
