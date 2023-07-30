import pika

from administrator.models import Admin
from base.models import BaseAbstractUser
from common.services.jwt.token import Token
from django.conf import settings
from django.test import TestCase
from faker import Faker
from rest_framework.test import APIClient

from customer.models import CustomerUser
from developer.models import CompanyUser
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
    def get_refresh_token(user: BaseAbstractUser) -> str:
        return Token().generate_refresh_token_for_user(user)

    @staticmethod
    def get_tokens(user: BaseAbstractUser) -> dict:
        return Token().generate_tokens_for_user(user)

    def get_user(self, user: BaseAbstractUser):

        data_user = self.__generate_data_for_users(user)

        if isinstance(user, CustomerUser):
            customer_user = CustomerUser.objects.create_user(**data_user)
            return customer_user
        elif isinstance(user, Admin):
            customer_user = Admin.objects.create_user(**data_user)
            return customer_user
        elif isinstance(user, CompanyUser):
            customer_user = CompanyUser.objects.create_user(**data_user)
            return customer_user
        else:
            raise ValueError(f"Type user {user.__class__.__name__} not found")

    def __generate_data_for_users(self, type_user: BaseAbstractUser) -> dict:
        data = {
            "username": self.faker.word(),
            "password": self.faker.word(),
            "email": self.faker.email(),
            "phone": self.faker.random_number(digits=10, fix_len=True),
        }
        if isinstance(type_user, CustomerUser):
            data["birthday"] = self.faker.date_object()
        return data
