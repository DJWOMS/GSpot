from typing import Type

from base.models import BaseAbstractUser
from base.notify.base_notify import BaseNotify
from utils.broker.message import NotifyMessage
from utils.broker.rabbitmq import RabbitMQ


class Notify(BaseNotify):
    rabbitmq = RabbitMQ()

    def send_notify(
        self,
        user: BaseAbstractUser,
        sender_user: BaseAbstractUser,
        message: Type[NotifyMessage],
    ):
        with self.rabbitmq as rabbit:
            rabbitmq_message = message(user=user, sender_user=sender_user)
            rabbit.send_message(rabbitmq_message)
