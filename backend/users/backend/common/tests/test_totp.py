import uuid
from datetime import datetime
from typing import Type
from unittest.mock import patch

from administrator.models import Admin
from base.models import BaseAbstractUser
from common.services.totp import TOTPToken
from config.settings import redis_config
from customer.models import CustomerUser
from developer.models import CompanyUser
from django.test import TestCase
from utils.db.redis_client import RedisTotpClient


class TestTOTPToken(TestCase):
    def setUp(self):
        self.r = RedisTotpClient(
            host=redis_config.REDIS_LOCAL_HOST,
            port=redis_config.REDIS_LOCAL_PORT,
            db=redis_config.REDIS_TOTP_DB,
            password=redis_config.REDIS_LOCAL_PASSWORD,
        )
        self.totp = TOTPToken()
        self.developer = self.create_user(CompanyUser)
        self.administrator = self.create_user(Admin)
        self.customer = self.create_user(CustomerUser)

    @staticmethod
    def create_user(user_model: Type[BaseAbstractUser]) -> Type[BaseAbstractUser]:
        data = {
            "username": "test_user",
            "password": "test_password",
            "email": "test_email@example.com",
            "phone": 12341234,
        }
        if user_model == CustomerUser:
            data["birthday"] = datetime.now()
        user = user_model.objects.create_user(**data)
        return user

    @patch("common.services.totp.totp.TOTPToken.generate_totp")
    def test_totp_for_developer(self, mock_generate_totp):
        test_token = str(uuid.uuid4())
        mock_generate_totp.return_value = test_token
        self.totp.send_totp(self.developer)

        encoded_data = self.r.is_token_exist(test_token)
        data = {key: value for key, value in encoded_data.items()}
        self.assertEqual(data["user_id"], str(self.developer.id))
        self.assertEqual(data["role"], self.developer._meta.app_label)

    @patch("common.services.totp.totp.TOTPToken.generate_totp")
    def test_totp_for_admin(self, mock_generate_totp):
        test_token = str(uuid.uuid4())
        mock_generate_totp.return_value = test_token
        self.totp.send_totp(self.administrator)

        encoded_data = self.r.is_token_exist(test_token)
        data = {key: value for key, value in encoded_data.items()}
        self.assertEqual(data["user_id"], str(self.administrator.id))
        self.assertEqual(data["role"], self.administrator._meta.app_label)

    @patch("common.services.totp.totp.TOTPToken.generate_totp")
    def test_totp_for_customer(self, mock_generate_totp):
        test_token = str(uuid.uuid4())
        mock_generate_totp.return_value = test_token
        self.totp.send_totp(self.customer)

        encoded_data = self.r.is_token_exist(test_token)
        data = {key: value for key, value in encoded_data.items()}
        self.assertEqual(data["user_id"], str(self.customer.id))
        self.assertEqual(data["role"], self.customer._meta.app_label)
