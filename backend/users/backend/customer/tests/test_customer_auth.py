import datetime
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from customer.models import CustomerUser


class DeveloperAuthViewTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        CustomerUser.objects.create_user(
            username="test_user",
            email="email@mail.ru",
            password="test_user1",
            first_name="user_test_name",
            last_name="user_test_name",
            phone="89991234567",
            is_active=True,
            birthday=datetime.date.today(),
        )
        cls.url = reverse("customer_login")

    def test_customer_auth_success(self):
        """
        Отправляем POST-запрос на аутентификацию с валидными учетными данными
        """
        data = {"email": "email@mail.ru", "password": "test_user1"}
        response = self.client.post(self.url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_customer_authentication_invalid_credentials(self):
        """
        Отправляем POST-запрос на аутентификацию с неправильными учетными данными
        """
        data = {"email": "wronguser", "password": "wrongpassword"}
        response = self.client.post(self.url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_customer_authentication_missing_fields(self):
        """
        Отправляем POST-запрос на аутентификацию без указания обязательных полей
        """
        data = {}
        response = self.client.post(self.url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
