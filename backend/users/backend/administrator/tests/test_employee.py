from django.contrib.auth.models import AbstractUser

from administrator.models import Admin
from base.base_tests.tests import BaseTestView
from django.test import TestCase
from common.models import Country


class EmployeeViewTest(BaseTestView, TestCase):
    url = '/api/v1/admin/employee/'
    valid_user: AbstractUser
    invalid_user: AbstractUser
    created: Admin

    @classmethod
    def setUpTestData(cls):
        Country.objects.create(id=1, name='Russia')
        cls.valid_user = Admin.objects.create_superuser(
            'admin3', 'admin2@admin.com', 'admin', '9803515667'
        )
        cls.invalid_user = Admin.objects.create_user('user', 'user1@user.com', 'user', '9804448971')
        cls.created = Admin.objects.create_user(
            'created_user', 'created_user@mail.com', 'created_user', '9803515227'
        )

    def test_01_create_employee(self):
        data = {
            "username": "user1",
            "first_name": "user1",
            "last_name": "user1",
            "email": "user1@example.com",
            "phone": "9804897651",
            "country": 1,
            "is_banned": False,
        }
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.valid_user))
        request = self.client.post(self.url, data)
        self.assertEqual(request.status_code, 201)

    def test_02_create_not_authorized_user(self):
        data = {
            "username": "user2",
            "first_name": "user2",
            "last_name": "user2",
            "email": "user2@example.com",
            "phone": "9824897651",
            "country": 1,
            "is_banned": False,
        }
        request = self.client.post(self.url, data)
        self.assertEqual(request.status_code, 403)

    def test_03_permissions(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.valid_user))
        request = self.client.get(self.url)
        self.assertEqual(request.status_code, 200)
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.invalid_user))
        request = self.client.get(self.url)
        self.assertEqual(request.status_code, 403)

    def test_04_get_retrieve(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.valid_user))
        request = self.client.get(f'{self.url}{self.created.id}/')
        self.assertEqual(request.status_code, 200)

    def test_05_partial_update(self):
        data = {'last_name': 'user3'}
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.valid_user))
        request = self.client.put(f'{self.url}{self.created.id}/', data)
        self.assertEqual(request.status_code, 200)
        self.assertEqual(Admin.objects.get(pk=self.created.id).last_name, data['last_name'])

    def test_06_delete(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.valid_user))
        request = self.client.delete(f'{self.url}{self.created.id}/')
        self.assertEqual(request.status_code, 204)
