from base.base_tests.test_base_get_jwt import GetJwtApiTestCase
from administrator.models import Admin
from rest_framework.test import APITestCase


class AdminGetJwtApiTestCase(GetJwtApiTestCase, APITestCase):
    @staticmethod
    def set_settings_user():
        user = {
            'username': 'user_of_company',
            'email': 'email@mail.ru',
            'password': 'usercompany',
            'first_name': 'user1',
            'last_name': 'user2',
            'phone': '89991234567',
        }
        return user

    @staticmethod
    def get_user_model():
        return Admin
