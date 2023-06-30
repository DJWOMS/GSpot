import uuid
from datetime import datetime
from typing import Type

from django.test import TestCase
from django.urls import reverse

from administrator.models import Admin
from base.models import BaseAbstractUser
from base.base_tests.tests import BaseTestView
from common.services.totp import TOTPToken
from customer.models import CustomerUser
from developer.models import CompanyUser
from utils.db.redis_client import RedisTotpClient
from config.settings import redis_config


class TestCheckTOTPToken(BaseTestView, TestCase):
    def setUp(self):
        self.check_totp_url = reverse('check-totp')
        self.set_password_url = reverse('totp-set-password')
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
        super().setUp()

    @staticmethod
    def create_user(user_model: Type[BaseAbstractUser]) -> Type[BaseAbstractUser]:
        data = {
            'username': 'test_user',
            'password': 'test_password',
            'email': 'test_email@example.com',
            'phone': 12341234,
        }
        if user_model == CustomerUser:
            data['birthday'] = datetime.now()
        user = user_model.objects.create_user(**data)
        return user

    def test_totp_for_developer(self):
        test_token = str(uuid.uuid4())
        self.totp.add_to_redis(test_token, self.developer)

        data = {'totp_token': test_token}
        request = self.client.post(self.check_totp_url, data=data)
        self.assertEqual(request.status_code, 200)

        data.update({'password': 12345})
        request = self.client.put(self.set_password_url, data=data)
        self.assertEqual(request.status_code, 201)

    def test_totp_for_admin(self):
        test_token = str(uuid.uuid4())
        self.totp.add_to_redis(test_token, self.administrator)

        data = {'totp_token': test_token}
        request = self.client.post(self.check_totp_url, data=data)
        self.assertEqual(request.status_code, 200)

        data.update({'password': 12345})
        request = self.client.put(self.set_password_url, data=data)
        self.assertEqual(request.status_code, 201)

    def test_totp_for_customer(
        self,
    ):
        test_token = str(uuid.uuid4())
        self.totp.add_to_redis(test_token, self.customer)

        data = {'totp_token': test_token}
        request = self.client.post(self.check_totp_url, data=data)
        self.assertEqual(request.status_code, 200)

        data.update({'password': 12345})
        request = self.client.put(self.set_password_url, data=data)
        self.assertEqual(request.status_code, 201)
