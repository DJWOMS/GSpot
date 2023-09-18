from base.base_tests.tests import BaseViewTestCase
from customer.models import CustomerUser
from django.urls import reverse
from rest_framework import status


class DeveloperAuthViewTestCase(BaseViewTestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse("customer_login")
        cls.password = cls.faker.word()
        cls.customer = CustomerUser.objects.create_user(
            username=cls.faker.word(),
            email=cls.faker.email(),
            password=cls.password,
            first_name=cls.faker.first_name(),
            last_name=cls.faker.last_name(),
            phone=cls.faker.random_number(digits=10, fix_len=True),
            birthday=cls.faker.date_object(),
            is_active=True,
        )

    def test_customer_auth_success(self):
        """
        Отправляем POST-запрос на аутентификацию с валидными учетными данными
        """
        data = {"email": self.customer.email, "password": self.password}
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
