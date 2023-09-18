import json
from dataclasses import dataclass, field

from base.models import BaseAbstractUser
from common import models
from django.conf import settings


@dataclass
class BaseMessage:
    user: BaseAbstractUser
    __message: dict[str] = field(init=False)

    def to_bytes(self) -> bytes:
        assert self.__message, 'message is not initialized'
        message_json = json.dumps(self.__message)
        return message_json.encode()

    def __post_init__(self, *args, **kwargs):
        self.__message = self.set_message(*args, **kwargs)

    def set_message(self, *args, **kwargs):
        raise NotImplementedError

    def get_message_from_db(self, *args, **kwargs):
        raise NotImplementedError


@dataclass
class EmailMessage(BaseMessage):
    subject: str
    exchange_name: str = settings.EMAIL_EXCHANGE_NAME
    routing_key: str = settings.EMAIL_ROUTING_KEY

    def set_message(self, *args, **kwargs):
        return {
            'email': self.user.email,
            'subject': self.subject,
            'body': self.get_message_from_db(),
        }


@dataclass
class NotifyMessage(BaseMessage):
    sender_user: BaseAbstractUser
    subject: str
    exchange_name: str = settings.NOTIFY_EXCHANGE_NAME
    routing_key: str = settings.NOTIFY_ROUTING_KEY

    def set_message(self, *args, **kwargs):
        return {
            'user_id': str(self.user.id),
            'subject': self.subject,
            'text': self.get_message_from_db().format(user=self.sender_user),
        }


@dataclass
class AdminActivationMessage(EmailMessage):
    totp: str = ...
    subject: str = 'admin_activation'

    def get_message_from_db(self, *args, **kwargs):
        instance = models.MessageEmailRabbitMQ.objects.get(
            action=models.MessageEmailRabbitMQ.DEVELOP_ACTIVATION,
        )
        text, url = instance.get_text
        return text.format(url=url.format(totp=self.totp))


@dataclass
class DevelopActivationMessage(EmailMessage):
    totp: str = ...
    subject: str = 'develop_activation'

    def get_message_from_db(self, *args, **kwargs):
        instance = models.MessageEmailRabbitMQ.objects.get(
            action=models.MessageEmailRabbitMQ.DEVELOP_ACTIVATION,
        )
        text, url = instance.get_text
        return text.format(url=url.format(totp=self.totp))


@dataclass
class CustomerActivationMessage(EmailMessage):
    totp: str = ...
    subject: str = 'customer_activation'

    def get_message_from_db(self, *args, **kwargs):
        instance = models.MessageEmailRabbitMQ.objects.get(
            action=models.MessageEmailRabbitMQ.DEVELOP_ACTIVATION,
        )
        text, url = instance.get_text
        return text.format(url=url.format(totp=self.totp))


@dataclass
class FriendAddedMessage(NotifyMessage):
    subject: str = 'Добавить в друзья'

    def get_message_from_db(self, *args, **kwargs):
        instance = models.MessageNotifyRabbitMQ.objects.get(
            action=models.MessageNotifyRabbitMQ.ADD_FRIEND,
        )
        return instance.get_text


@dataclass
class TOTPTokenMessage(BaseMessage):
    exchange_name: str = settings.TOTP_EXCHANGE_NAME
    routing_key: str = settings.TOTP_ROUTING_KEY
