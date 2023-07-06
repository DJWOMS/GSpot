from base.models import BaseAbstractUser
from base.notify.base_notify import BaseNotify
from utils.broker.message import FriendAddedMessage
from utils.broker.rabbitmq import RabbitMQ


class Notify(BaseNotify):
    rabbitmq = RabbitMQ()
    message = FriendAddedMessage

    def send_notify(self, user: BaseAbstractUser, sender_user: BaseAbstractUser):
        with self.rabbitmq as rabbit:
            rabbitmq_message = self.message(user=user, sender_user=sender_user)
            rabbit.send_message(rabbitmq_message)
