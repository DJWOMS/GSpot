import datetime

from django.contrib.auth.models import AbstractUser

from administrator.models import Admin
from base.base_tests.tests import BaseTestView
from django.test import TestCase
from common.models import Country
from customer.models import CustomerUser


class CustomersViewTest(BaseTestView, TestCase):
    url = '/api/v1/admin/customers'
    user: AbstractUser
    created: Admin

    @classmethod
    def setUpTestData(cls):
        Country.objects.create(id=1, name='Russia')
        cls.created = Admin.objects.create_superuser(
            'admin3', 'admin2@admin.com', 'admin', '9803515667'
        )
        cls.user = CustomerUser.objects.create_user(
            username="test_user",
            email="email@mail.ru",
            password="test_user1",
            first_name="user_test_name",
            last_name="user_test_name",
            phone="89991234567",
            birthday=datetime.date.today(),
        )

    def test_01_block_customer(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.user))
        request = self.client.post(f"{self.url}/{self.user.id}/block", {'reason': 'Test reason'})
        self.assertEqual(request.status_code, 201)

    def test_02_unblock_customer(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.user))
        request = self.client.post(f"{self.url}/{self.user.id}/unblock")
        self.assertEqual(request.status_code, 200)

    def test_03_delete(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.user))
        request = self.client.delete(f'{self.url}/{self.user.id}/')
        self.assertEqual(request.status_code, 204)
