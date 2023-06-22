from faker import Faker

from django.urls import reverse

from administrator.models import Admin
from base.base_tests.tests import BaseTestView
from django.test import TestCase
from common.models import Country
from developer.models import Company, CompanyUser

fake = Faker(locale='ru_RU')


class CompanyViewTest(BaseTestView, TestCase):
    url = reverse('admin_company')
    admin: Admin
    user: CompanyUser
    company: Company

    @classmethod
    def setUpTestData(cls):
        Country.objects.create(id=1, name=fake.country())
        cls.admin = Admin.objects.create_superuser(
            fake.first_name(), fake.email(), fake.word(), '89991112233'
        )
        cls.user = CompanyUser.objects.create_user(
            username=fake.word(),
            email=fake.email(),
            password=fake.word(),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            phone='89991112239',
        )
        cls.company = Company.objects.create(
            created_by=cls.user,
            title=fake.text(max_nb_chars=50),
            description=fake.text(),
            email=fake.email(),
        )

    def test_000_list_company(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.admin))
        request = self.client.get(self.url)
        self.assertEqual(request.status_code, 200)

    def test_01_block_company(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.admin))
        payload = {'reason': fake.text()}
        request = self.client.post(f"{self.url}{self.company.id}/block", payload, format='json')
        self.assertEqual(request.status_code, 201)

    def test_02_unblock_company(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.admin))
        payload = {'reason': fake.text()}
        self.company.is_banned = True
        self.company.save()
        request = self.client.post(f"{self.url}{self.company.id}/unblock", payload, format='json')
        self.assertEqual(request.status_code, 201)

    def test_03_delete(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.admin))
        request = self.client.delete(f'{self.url}{self.company.id}/')
        self.assertEqual(request.status_code, 204)
