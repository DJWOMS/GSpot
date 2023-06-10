from datetime import datetime
from django.test import TestCase
from typing import Type

from administrator.models import Admin
from base.models import BaseAbstractUser
from common.services.jwt.users_payload import PayloadFactory
from customer.models import CustomerUser
from developer.models import CompanyUser


class TestTokenJWT(TestCase):
    def setUp(self):
        self.payload_factory = PayloadFactory()
        self.developer = self.create_user(CompanyUser)
        self.administrator = self.create_user(Admin)
        self.customer = self.create_user(CustomerUser)

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

    def test_admin_payload(self):
        payload = self.payload_factory.create_payload(self.administrator)
        self.assertIsInstance(payload, dict)

    def test_developer_payload(self):
        payload = self.payload_factory.create_payload(self.developer)
        self.assertIsInstance(payload, dict)

    def test_customer_payload(self):
        payload = self.payload_factory.create_payload(self.customer)
        self.assertIsInstance(payload, dict)

    def test_not_base_abstract_user_instance(self):
        self.assertRaises(TypeError, self.payload_factory.create_payload, str)
