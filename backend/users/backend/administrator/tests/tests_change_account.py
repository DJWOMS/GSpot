from base.base_tests.change_account_info_tests_base import ChangeAccountInfoApiTestCase
from rest_framework.test import APITestCase
from administrator.models import Admin


class AdminChangeAccountInfoApiTestCase(ChangeAccountInfoApiTestCase, APITestCase):
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

    @staticmethod
    def get_reverse_url():
        return 'administrator-user-account'
