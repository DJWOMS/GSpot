from datetime import datetime

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from administrator.models import Admin
from base.models import BaseAbstractUser
from common.services.jwt.token import Token
from customer.models import CustomerUser
from developer.models import CompanyUser


class TestJWTLogoutView(TestCase):
    def setUp(self):
        self.token = Token()
        self.path = reverse('logout')
        self.client = APIClient()
        self.invalid_token = {"refresh_token": "testinvalidrefreshtoken"}

    def test_logout_developer(self):
        refresh_token = self.create_refresh_token(CompanyUser)
        response = self.client.post(self.path, refresh_token, format='json')
        self.assertEqual(response.status_code, 205)

    def test_logout_admin(self):
        refresh_token = self.create_refresh_token(Admin)
        response = self.client.post(self.path, refresh_token, format='json')
        self.assertEqual(response.status_code, 205)

    def test_logout_customer(self):
        refresh_token = self.create_refresh_token(CustomerUser)
        response = self.client.post(self.path, refresh_token, format='json')
        self.assertEqual(response.status_code, 205)

    @staticmethod
    def create_refresh_token(user_model: type[BaseAbstractUser]) -> dict:
        data = {
            'username': 'test_user',
            'password': 'test_password',
            'email': 'test_email@example.com',
        }
        if user_model == CustomerUser:
            data['birthday'] = datetime.now()
        user = user_model.objects.create(**data)
        user_data = {'user_id': str(user.id), 'role': user_model._meta.app_label}
        refresh_token = Token().generate_refresh_token(user_data)
        return {'refresh_token': refresh_token}

    def test_logout_with_invalid_token(self):
        response = self.client.post(self.path, self.invalid_token, format='json')
        self.assertEqual(response.status_code, 400)

    def test_logout_without_token(self):
        response = self.client.post(self.path)
        self.assertEqual(response.status_code, 400)
