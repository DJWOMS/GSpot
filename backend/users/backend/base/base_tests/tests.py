from base.models import BaseAbstractUser
from common.services.jwt.token import Token
from django.test import TestCase
from faker import Faker
from rest_framework.test import APIClient


class BaseTestView(TestCase):
    faker = Faker(locale='ru_RU')

    def setUp(self) -> None:
        self.client = APIClient()

    @staticmethod
    def get_token(user: BaseAbstractUser) -> str:
        return Token().generate_access_token_for_user(user)

    @staticmethod
    def get_tokens(user: BaseAbstractUser) -> dict:
        return Token().generate_tokens_for_user(user)
