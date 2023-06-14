from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from developer.models import CompanyUser


class DeveloperAuthViewTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        CompanyUser.objects.create_user(
            username="user_of_company",
            email="email@mail.ru",
            password="usercompany",
            first_name="user1",
            last_name="user2",
            phone="89991234567",
            is_active=True,
            company=None,
        )
        cls.url = reverse("developer_login")

    def test_developer_authentication_success(self):
        """
        Отправляем POST-запрос на аутентификацию с валидными учетными данными
        """
        data = {"email": "email@mail.ru", "password": "usercompany"}

        response = self.client.post(self.url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_developer_authentication_invalid_credentials(self):
        """
        Отправляем POST-запрос на аутентификацию с неправильными учетными данными
        """
        data = {"username": "testuser", "password": "wrongpassword"}
        response = self.client.post(self.url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_developer_authentication_missing_fields(self):
        """
        Отправляем POST-запрос на аутентификацию без указания обязательных полей
        """
        data = {}
        response = self.client.post(self.url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
