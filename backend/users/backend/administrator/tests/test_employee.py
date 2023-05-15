from django.contrib.auth.models import AbstractUser

from administrator.models import Admin
from base.base_tests.tests import TestDataSet, TestView, TestBase
from django.test import TestCase
from rest_framework.test import APIClient
from common.models import Country
from common.services.jwt.token import Token


class EmployeeViewTest(TestCase):
    url = '/api/v1/admin/employee/'
    valid_user: AbstractUser
    invalid_user: AbstractUser

    def setUp(self) -> None:
        self.client = APIClient()

    @classmethod
    def setUpTestData(cls):
        Country.objects.create(id=1, name='Russia')
        cls.valid_user = Admin.objects.create_superuser(
            'admin3', 'admin2@admin.com', 'admin', '9803515667'
        )
        cls.invalid_user = Admin.objects.create_user('user', 'user1@user.com', 'user', '9804448971')

    @staticmethod
    def authenticate(user) -> str:
        context = {
            'user_id': str(user.id),
            'role': user._meta.app_label,
        }
        return Token().generate_access_token(context)

    def test_create_employee(self):
        valid_data = {
            "username": "user1",
            "first_name": "user1",
            "last_name": "user1",
            "email": "user1@example.com",
            "phone": "9804897651",
            "country": 1,
            "is_banned": False,
        }
        self.client.credentials(HTTP_AUTHORIZATION=self.authenticate(self.valid_user))
        request = self.client.post(self.url, valid_data)
        self.assertEqual(request.status_code, 201)

    def test_permissions(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.authenticate(self.valid_user))
        request = self.client.get(self.url)
        self.assertEqual(request.status_code, 200)
        self.client.credentials(HTTP_AUTHORIZATION=self.authenticate(self.invalid_user))
        request = self.client.get(self.url)
        self.assertEqual(request.status_code, 403)
