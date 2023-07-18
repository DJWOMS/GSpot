import pika
from base.models import BaseAbstractUser
from common.services.jwt.token import Token
from django.conf import settings
from django.test import TestCase
from faker import Faker
from rest_framework.test import APIClient
from utils.broker.rabbitmq import RabbitMQ


class BaseViewTestCase(TestCase):
    faker = Faker(locale='ru_RU')

    def setUp(self) -> None:
        self.client = APIClient()

    def tearDown(self) -> None:
        self.rabbitmq = RabbitMQ()
        with self.rabbitmq:
            try:
                self.rabbitmq._channel.queue_purge(queue=settings.EMAIL_ROUTING_KEY)
            except (pika.exceptions.ChannelClosedByBroker, pika.exceptions.ChannelWrongStateError):
                pass
            try:
                self.rabbitmq._channel.queue_purge(queue=settings.NOTIFY_ROUTING_KEY)
            except (pika.exceptions.ChannelClosedByBroker, pika.exceptions.ChannelWrongStateError):
                pass

    @staticmethod
    def get_access_token(user: BaseAbstractUser) -> str:
        return Token().generate_access_token_for_user(user)

    @staticmethod
    def get_tokens(user: BaseAbstractUser) -> dict:
        return Token().generate_tokens_for_user(user)
