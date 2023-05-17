from django.test import TestCase

from administrator.models import Admin
from base.base_tests.tests import BaseTestView
from common.models import Country, ContactType
from developer.models import Company, CompanyUser


class DeveloperTestView(BaseTestView, TestCase):
    url = '/api/v1/developer/employee/'
    company_owner: CompanyUser

    @classmethod
    def setUpTestData(cls):
        Country.objects.create(id=1, name='Russia')
        cls.company_owner = CompanyUser.objects.create_user(
            'company_owner',
            'company_owner@mail.ru',
            '9803489988',
            'company_owner',
        )
        company = Company.objects.create(
            id=1,
            created_by=cls.company_owner,
            title='company',
            description='company_description',
            email='company@email.com',
            is_confirmed=True,
            is_active=True,
        )
        cls.company_owner.company = company
        cls.company_owner.save()

    def test_010_create_employee(self):
        data = {
            "username": "company_user1",
            "first_name": "company_user1",
            "last_name": "company_user1",
            "email": "company_user@example.com",
            "phone": "9803449861",
            "country": 1,
            "is_banned": False,
        }
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.company_owner))
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 201)

    def test_020_get_list_by_company_owner(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.company_owner))
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_030_check_permission_not_authorized_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 403)
