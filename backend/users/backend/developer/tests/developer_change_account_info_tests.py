from base.base_tests.change_account_info_tests_base import ChangeAccountInfoApiTestCase
from rest_framework.test import APITestCase
from developer.models import CompanyUser


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
            'company': None,
        }
        return user

    @staticmethod
    def get_user_model():
        return CompanyUser

    @staticmethod
    def get_reverse_url():
        return 'developer-user-account'
