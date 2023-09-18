from administrator.models import Admin
from base.base_tests.tests import BaseViewTestCase
from django.urls import reverse
from rest_framework import status


class AdminAuthViewTestCase(BaseViewTestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse("admin_login")
        cls.password = cls.faker.word()
        cls.admin_user = Admin.objects.create_user(
            username=cls.faker.first_name(),
            password=cls.password,
            email=cls.faker.email(),
            phone=cls.faker.random_number(digits=10, fix_len=True),
        )

    def test_000_admin_authentication_success(self):
        """
        Отправляем POST-запрос на аутентификацию с валидными учетными данными
        """
        data = {"email": self.admin_user.email, "password": self.password}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_01_admin_authentication_invalid_credentials(self):
        """
        Отправляем POST-запрос на аутентификацию с неправильными учетными данными
        """
        data = {"username": self.admin_user.username, "password": self.faker.word()}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_02_admin_authentication_missing_fields(self):
        """
        Отправляем POST-запрос на аутентификацию без указания обязательных полей
        """
        data = {}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
