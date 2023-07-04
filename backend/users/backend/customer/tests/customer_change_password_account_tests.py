import datetime

from base.base_tests.change_password_account_base import (
    ChangePasswordAccountInfoApiTestCase,
)
from customer.models import CustomerUser
from rest_framework.test import APITestCase


class CustomerChangePasswordApiTestCase(ChangePasswordAccountInfoApiTestCase, APITestCase):
    @staticmethod
    def set_settings_user():
        user = {
            "username": "user_of_company",
            "email": "email@mail.ru",
            "password": "usercompany",
            "first_name": "user1",
            "last_name": "user2",
            "phone": "89991234567",
            "birthday": datetime.date.today(),
        }
        return user

    @staticmethod
    def get_user_model():
        return CustomerUser

    @staticmethod
    def get_reverse_url():
        return "customer-user-change-password"
