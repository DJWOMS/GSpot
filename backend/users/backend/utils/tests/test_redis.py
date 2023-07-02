from datetime import datetime
from typing import Type

from administrator.models import Admin
from base.models import BaseAbstractUser
from common.services.jwt.users_payload import PayloadFactory
from config.settings import redis_config
from customer.models import CustomerUser
from developer.models import CompanyUser
from django.test import TestCase
from utils.db.redis_client import RedisAccessClient, RedisRefreshClient, RedisTotpClient


class RedisClientTestCase(TestCase):
    def setUp(self) -> None:
        host = (redis_config.REDIS_LOCAL_HOST,)
        port = (redis_config.REDIS_LOCAL_PORT,)
        password = redis_config.REDIS_LOCAL_PASSWORD
        access_db = redis_config.REDIS_ACCESS_DB
        refresh_db = redis_config.REDIS_REFRESH_DB
        totp_db = redis_config.REDIS_TOTP_DB

        self.developer = self.create_user(CompanyUser)
        self.administrator = self.create_user(Admin)
        self.customer = self.create_user(CustomerUser)
        self.redis_access_client = RedisAccessClient(
            host=host,
            port=port,
            db=access_db,
            password=password,
        )
        self.redis_refresh_client = RedisRefreshClient(
            host=host,
            port=port,
            db=refresh_db,
            password=password,
        )
        self.redis_totp_client = RedisTotpClient(
            host=host,
            port=port,
            db=totp_db,
            password=password,
        )
        self.redis_access_client_basik = RedisAccessClient(
            host=host,
            port=port,
            db=3,
            password=password,
        )
        self.redis_refresh_client_basik = RedisRefreshClient(
            host=host,
            port=port,
            db=3,
            password=password,
        )
        self.redis_totp_client_basik = RedisTotpClient(
            host=host,
            port=port,
            db=3,
            password=password,
        )

    @staticmethod
    def create_user(user_model: Type[BaseAbstractUser]) -> Type[BaseAbstractUser]:
        data = {
            "username": "test_user",
            "password": "test_password",
            "email": "test_email@example.com",
            "phone": 12341234,
            "is_active": True,
        }
        if user_model == CustomerUser:
            data["birthday"] = datetime.now()
        user = user_model.objects.create_user(**data)
        return user

    @staticmethod
    def get_user_payload(user: BaseAbstractUser) -> dict:
        factory = PayloadFactory()
        return factory.create_payload(user)

    def test_add_access_token(self):
        self.redis_access_client.add_token(token="test_access_token_one")
        result = self.redis_access_client.is_token_exist(token="test_access_token_one")
        self.assertEqual(bool(result), True)

    def test_is_token_exist_false(self):
        result = self.redis_access_client.is_token_exist(token="this_token_false")
        self.assertEqual(bool(result), False)

    def test_add_refresh_token(self):
        self.redis_refresh_client.add_token(token="test_refresh_token_one")
        result = self.redis_refresh_client.is_token_exist(token="test_refresh_token_one")
        self.assertEqual(bool(result), True)

    def test_refresh_in_access(self):
        result_access = self.redis_access_client.is_token_exist(
            token="refresh:test_refresh_token_one",
            prefix=False,
        )
        result_refresh = self.redis_refresh_client.is_token_exist(
            token="access:test_access_token_one",
            prefix=False,
        )
        self.assertEqual(bool(result_access), False)
        self.assertEqual(bool(result_refresh), False)

    def test_add_totp_token(self):
        self.redis_totp_client.add_token(token="test_totp_token_one")
        result = self.redis_totp_client.is_token_exist(token="test_totp_token_one")
        self.assertEqual(bool(result), True)

    def test_is_token_exist_totp_token(self):
        result_access = self.redis_access_client.is_token_exist(
            token="totp:test_totp_token_one",
            prefix=False,
        )
        result_refresh = self.redis_refresh_client.is_token_exist(
            token="totp:test_totp_token_one",
            prefix=False,
        )
        result_totp = self.redis_totp_client.is_token_exist(token="wrong_totp_token")

        self.assertEqual(bool(result_refresh), False)
        self.assertEqual(bool(result_access), False)
        self.assertEqual(bool(result_totp), False)

    def test_all_tokens_in_one_db(self):
        self.redis_access_client_basik.add_token(token="access_one")
        self.redis_refresh_client_basik.add_token(token="refresh_one")
        self.redis_totp_client_basik.add_token(token="totp_one")
        result_access = self.redis_totp_client_basik.is_token_exist(
            token="access:access_one",
            prefix=False,
        )
        result_refresh = self.redis_access_client_basik.is_token_exist(
            token="refresh:refresh_one",
            prefix=False,
        )
        result_totp = self.redis_refresh_client_basik.is_token_exist(
            token="totp:totp_one",
            prefix=False,
        )

        self.assertEqual(bool(result_access), True)
        self.assertEqual(bool(result_refresh), True)
        self.assertEqual(bool(result_totp), True)

    def test_dict_in_access(self):
        data = {
            "type": "access",
            "permissions": "admins",
            "image": "12",
            "list": ["1", 1],
        }
        self.redis_access_client.add_token(token="12345", value=data)
        result = self.redis_access_client.is_token_exist(token="12345")
        result_data = {key: value for key, value in result.items()}

        self.assertEqual(bool(result), True)
        self.assertEqual(result_data["type"], data["type"])
        self.assertEqual(result_data["permissions"], data["permissions"])
        self.assertEqual(result_data["image"], data["image"])
        self.assertEqual(result_data["list"], data["list"])
