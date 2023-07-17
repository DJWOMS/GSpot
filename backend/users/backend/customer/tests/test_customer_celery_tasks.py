import datetime

from celery.result import AsyncResult
from customer.models import CustomerUser
from customer.tasks import create_payment_account
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class DeveloperAuthViewTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.data_customer_user = {
            "username": "test_user",
            "email": "email@mail.ru",
            "password": "test_user1",
            "first_name": "user_test_name",
            "last_name": "user_test_name",
            "phone": "89991234567",
            "is_active": True,
            "birthday": datetime.date.today(),
        }
        cls.customer: CustomerUser = CustomerUser.objects.create_user(
            username="test_user",
            email="email@mail.ru",
            password="test_user1",
            first_name="user_test_name",
            last_name="user_test_name",
            phone="89991234567",
            is_active=True,
            birthday=datetime.date.today(),
        )
        cls.url = reverse("customer_registration")

    def test_000_registration_success(self):
        result = create_payment_account.delay(self.customer.id)
        self.assertIsInstance(result, AsyncResult)
