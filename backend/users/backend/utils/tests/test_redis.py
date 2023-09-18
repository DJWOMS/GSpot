from datetime import datetime
from typing import Type

from administrator.models import Admin
from base.base_tests.tests import BaseViewTestCase
from base.models import BaseAbstractUser
from common.services.jwt.users_payload import PayloadFactory
from config.settings import redis_config
from customer.models import CustomerUser
from developer.models import CompanyUser
from utils.db.redis_client import RedisAccessClient, RedisRefreshClient, RedisTotpClient


class RedisClientTestCase(BaseViewTestCase):
    @classmethod
    def setUpTestData(cls):
        cls.developer = cls.create_user(CompanyUser)
        cls.administrator = cls.create_user(Admin)
        cls.customer = cls.create_user(CustomerUser)

    def setUp(self) -> None:
        host = (redis_config.REDIS_LOCAL_HOST,)
        port = (redis_config.REDIS_LOCAL_PORT,)
        password = redis_config.REDIS_LOCAL_PASSWORD
        access_db = redis_config.REDIS_ACCESS_DB
        refresh_db = redis_config.REDIS_REFRESH_DB
        totp_db = redis_config.REDIS_TOTP_DB
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

    @classmethod
    def create_user(cls, user_model: Type[BaseAbstractUser]) -> Type[BaseAbstractUser]:
        data = {
            "username": cls.faker.first_name(),
            "password": cls.faker.word(),
            "email": cls.faker.email(),
            "phone": cls.faker.random_number(digits=10, fix_len=True),
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

    def test_is_token_exist_totptoken(self):
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

    def test_long_token(self):
        token = """eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzI
                iwiaWF0IjoxNjg4MDU5NTI2LCJleHAiOjE2ODgwNTk4MjYsInVzZXJfaWQiOiJjNzRlZG
                Y1MC1kNTUzLTRiYWMtYmUzZi04MjNmMzlmMTE4YWUiLCJyb2xlIjoiYWRtaW5pc3RyYXR
                vciIsImF2YXRhciI6IiIsInBlcm1pc3Npb25zIjpbXSwiZW1haWwiOiJ0ZXN0X2VtYWls
                QGV4YW1wbGUuY29tIiwicGhvbmUiOjEyMzQxMjM0LCJjb3VudHJ5IjpudWxsLCJjcmVhd
                GVkX2F0IjoiMjAyMy0wNi0yOSAxNzoyNToyNi42MTg3MzgrMDA6MDAiLCJ1cGRhdGVfYX
                QiOiIyMDIzLTA2LTI5IDE3OjI1OjI2LjYxODc0OSswMDowMCIsImlzX3N1cGVydXNlciI
                6ZmFsc2UsImdyb3VwcyI6W10sInVzZXJfcGVybWlzc2lvbnMiOltdLCJkZXZlbG9wZXJf
                Z3JvdXBzIjpbXSwiZGV2ZWxvcGVyX3Blcm1pc3Npb25zIjpbXX0.aijkwQOwY91Tk2DFi
                gfkSy6zmKHa6m1ADIv27-TdDzM"""
        data = {"type": "access"}
        self.redis_access_client.add_token(token=token, value=data)
        result = self.redis_access_client.is_token_exist(token=token)
        result_data = {key: value for key, value in result.items()}

        self.assertEqual(bool(result), True)
        self.assertEqual(result_data["type"], data["type"])

    def test_create_and_check_token_admin(self):
        admin_payload_data = self.get_user_payload(self.administrator)
        self.redis_access_client.add_token(token="admin_test_token", value=admin_payload_data)
        result = self.redis_access_client.is_token_exist(token="admin_test_token")
        result_data = {key: value for key, value in result.items()}
        self.maxDiff = None
        self.assertEqual(result_data, admin_payload_data)

    def test_create_and_check_token_customer(self):
        customer_payload_data = self.get_user_payload(self.customer)
        self.redis_access_client.add_token(token="customer_test_token", value=customer_payload_data)
        result = self.redis_access_client.is_token_exist(token="customer_test_token")
        result_data = {key: value for key, value in result.items()}
        self.maxDiff = None
        self.assertEqual(result_data, customer_payload_data)

    def test_create_and_check_token_developer(self):
        developer_payload_data = self.get_user_payload(self.developer)
        self.redis_access_client.add_token(
            token="developer_test_token",
            value=developer_payload_data,
        )
        result = self.redis_access_client.is_token_exist(token="developer_test_token")
        result_data = {key: value for key, value in result.items()}
        self.maxDiff = None
        self.assertEqual(result_data, developer_payload_data)
