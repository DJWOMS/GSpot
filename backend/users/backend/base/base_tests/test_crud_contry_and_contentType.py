import datetime
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from common.services.jwt.token import Token
from administrator.models import Admin
from base.base_tests.tests import BaseTestView
from customer.models import CustomerUser


class MixinTestView:
    client = APIClient()

    @staticmethod
    def get_token(user) -> str:
        context = {
            "user_id": str(user.id),
            "role": user._meta.app_label,
        }
        return Token().generate_access_token(context)

    @classmethod
    def test_list(cls, user, test: TestCase):
        cls.client.credentials(HTTP_AUTHORIZATION=cls.get_token(user))
        response = cls.client.get(f"{test.url}")
        test.assertEqual(response.status_code, status.HTTP_200_OK)

    @classmethod
    def test_list_not_credentials(cls, test: TestCase):
        cls.client.credentials(HTTP_AUTHORIZATION="")
        response = cls.client.get(f"{test.url}")
        test.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    @classmethod
    def test_retrive(cls, pk: int, user, test: TestCase):
        cls.client.credentials(HTTP_AUTHORIZATION=cls.get_token(user))
        response = cls.client.get(f"{test.url}{pk}/")
        test.assertEqual(response.status_code, status.HTTP_200_OK)

    @classmethod
    def test_delete(cls, pk, user, test: TestCase):
        cls.client.credentials(HTTP_AUTHORIZATION=cls.get_token(user))
        response = cls.client.delete(f"{test.url}{pk}/")
        test.assertEqual(response.status_code, 204)

    @classmethod
    def test_create(cls, user, data, test: TestCase):
        cls.client.credentials(HTTP_AUTHORIZATION=cls.get_token(user))
        response = cls.client.post(test.url, data)
        test.assertEqual(response.status_code, 201)

    @classmethod
    def test_put(cls, pk: int, user, data, test: TestCase):
        cls.client.credentials(HTTP_AUTHORIZATION=cls.get_token(user))
        response = cls.client.put(f"{test.url}{pk}/", data)
        test.assertEqual(response.status_code, status.HTTP_200_OK)


class BaseViewSetTestCase(BaseTestView, TestCase):
    url: str = ""
    admin_user: Admin
    user: CustomerUser

    class Meta:
        view: MixinTestView = MixinTestView

    def setUp(self):
        self.admin_user = Admin.objects.create_superuser(
            username="adminR",
            email="adminR@test.com",
            phone="891123123",
            password="testpass123R",
        )
        self.user = CustomerUser.objects.create_user(
            username="test_user",
            email="email@mail.ru",
            password="test_user1",
            first_name="user_test_name",
            last_name="user_test_name",
            phone="89991234567",
            birthday=datetime.date.today(),
        )
        super().setUp()
