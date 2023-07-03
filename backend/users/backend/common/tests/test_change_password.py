import datetime

from administrator.models import Admin
from base.base_tests.tests import BaseTestView
from customer.models import CustomerUser
from developer.models import CompanyUser
from django.test import TestCase
from django.urls import reverse
from rest_framework import status


class ChangePassTestAPI(BaseTestView, TestCase):
    url = reverse("user_change_password")
    admin_user: Admin
    customer_user: CustomerUser
    developer: CompanyUser

    @classmethod
    def setUpTestData(cls):
        cls.admin_user = Admin.objects.create_superuser(
            username="adminR",
            email="adminR@test.com",
            phone="891123123",
            password="testpassAdmin123R",
            is_active=True,
        )
        cls.customer_user = CustomerUser.objects.create_user(
            username="customer_user",
            email="email@mail.ru",
            password="test_customer_user1",
            first_name="user_test_name",
            last_name="user_test_name",
            phone="89991234567",
            birthday=datetime.date.today(),
            is_active=True,
        )
        cls.developer = CompanyUser.objects.create_user(
            username="test super_user",
            email="testuser@example.com",
            phone="1234567890",
            password="testpassword",
            is_active=True,
            is_superuser=True,
        )

    def test_developer_change_password_currect_patch(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.developer))
        data = {
            "old_password": "testpassword",
            "new_password": "adminnew01",
            "confirmation_new_password": "adminnew01",
        }
        response = self.client.post(self.url, data=data, format="json")
        user: CompanyUser = CompanyUser.objects.get(username=self.developer.username)

        self.assertTrue(user.check_password("adminnew01"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_developer_change_password_wrong_old_password(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.developer))
        data = {
            "old_password": "wrongpassword",
            "new_password": "developernew01",
            "confirmation_new_password": "developernew01",
        }
        response = self.client.post(self.url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_developer_change_password_wrong_confirm_password(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.developer))
        data = {
            "old_password": "testpassword",
            "new_password": "Gachidevelopernew01",
            "confirmation_new_password": "NOGachidevelopernew01",
        }
        response = self.client.post(self.url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_change_password_unauthenticate_user(self):
        self.client.credentials(HTTP_AUTHORIZATION="")
        data = {
            "old_password": "somepassword",
            "new_password": "adminnew01",
            "confirmation_new_password": "adminnew01",
        }
        response = self.client.post(self.url, data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_costumer_user_change_password_currect_patch(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.customer_user))
        data = {
            "old_password": "test_customer_user1",
            "new_password": "gachiActor1",
            "confirmation_new_password": "gachiActor1",
        }
        response = self.client.post(self.url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user: CustomerUser = CustomerUser.objects.get(username=self.customer_user.username)

        self.assertTrue(user.check_password("gachiActor1"))

    def test_admin_user_change_password_currect_patch(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.admin_user))
        data = {
            "old_password": "testpassAdmin123R",
            "new_password": "gachiAdmin12ru",
            "confirmation_new_password": "gachiAdmin12ru",
        }
        response = self.client.post(self.url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user: Admin = Admin.objects.get(username=self.admin_user.username)

        self.assertTrue(user.check_password("gachiAdmin12ru"))
