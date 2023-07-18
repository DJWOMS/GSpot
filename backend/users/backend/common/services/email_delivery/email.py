from base.delivery.base_email import BaseEmail
from utils.broker.message import BaseMessage
from utils.broker.rabbitmq import RabbitMQ


class EmailDelivery(BaseEmail):
    rabbitmq = RabbitMQ()

    def send_email(
        self,
        message: BaseMessage,
    ):
        with self.rabbitmq as rabbit:
            rabbit.send_message(message=message)
