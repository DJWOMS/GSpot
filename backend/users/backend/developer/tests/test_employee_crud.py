from django.test import TestCase

from administrator.models import Admin
from base.base_tests.tests import BaseTestView
from common.models import Country, ContactType
from developer.models import Company, CompanyUser


class DeveloperTestView(BaseTestView, TestCase):
    url = '/api/v1/developer/employee/'
    company_owner: CompanyUser
    created: CompanyUser

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
        cls.created = CompanyUser.objects.create_user(
            'company_user',
            'company_user@example.com',
            '9807789345',
            'company_user',
            company=company,
        )

    def test_010_create_employee(self):
        data = {
            "username": "company_user1",
            "first_name": "company_user1",
            "last_name": "company_user1",
            "email": "company_user1@example.com",
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

    def test_040_get_developer_detail(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.company_owner))
        response = self.client.get(f'{self.url}{self.created.id}/')
        self.assertEqual(response.status_code, 200)

    def test_050_partial_update_developer(self):
        data = {
            "first_name": '123',
        }
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.company_owner))
        response = self.client.put(f'{self.url}{self.created.id}/', data)
        self.assertEqual(response.status_code, 200)

    def test_060_queryset(self):
        test_company_owner = CompanyUser.objects.create_user(
            'company_owner2',
            'company_owner2@mail.ru',
            '9803484188',
            'company_owner2',
        )
        test_company = Company.objects.create(
            id=2,
            created_by=test_company_owner,
            title='company2',
            description='company_description2',
            email='company2@email.com',
            is_confirmed=True,
            is_active=True,
        )
        test_company_owner.company = test_company
        test_company_owner.save()
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(test_company_owner))
        response = self.client.get(self.url)
        self.assertEqual(len(response.data), 0)
        response = self.client.get(f'{self.url}{self.created.id}/')
        self.assertEqual(response.status_code, 404)
