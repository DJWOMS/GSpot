from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from administrator.models import Admin


class AdminAuthViewTestCase(APITestCase):
    def setUp(self):
        self.url = reverse("admin_login")

    def test_admin_authentication_success(self):
        """
        Отправляем POST-запрос на аутентификацию с валидными учетными данными
        """

        Admin.objects.create_user(
            username="testuser",
            password="password",
            email="test@example.com",
            phone="9998887766",
        )

        data = {"email": "test@example.com", "password": "password"}

        response = self.client.post(self.url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_admin_authentication_invalid_credentials(self):
        """
        Отправляем POST-запрос на аутентификацию с неправильными учетными данными
        """
        data = {"username": "testuser", "password": "wrongpassword"}
        response = self.client.post(self.url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_admin_authentication_missing_fields(self):
        """
        Отправляем POST-запрос на аутентификацию без указания обязательных полей
        """

        data = {}

        response = self.client.post(self.url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
