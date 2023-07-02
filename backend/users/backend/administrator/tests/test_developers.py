from administrator.models import Admin
from base.base_tests.tests import BaseTestView
from common.models import Country
from developer.models import CompanyUser
from django.contrib.auth.models import AbstractUser
from django.test import TestCase
from django.urls import reverse
from faker import Faker

fake = Faker(locale="ru_RU")


class DevelopersViewTest(BaseTestView, TestCase):
    url = reverse("admin_developers")
    user: AbstractUser
    admin: Admin

    @classmethod
    def setUpTestData(cls):
        Country.objects.create(id=1, name=fake.country())
        cls.admin = Admin.objects.create_superuser(
            fake.first_name(),
            fake.email(),
            fake.word(),
            "89991112235",
        )
        cls.user = CompanyUser.objects.create_user(
            username=fake.word(),
            email=fake.email(),
            password=fake.word(),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            phone="89991112237",
        )

    def test_000_list_developer(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.admin))
        request = self.client.get(self.url)
        self.assertEqual(request.status_code, 200)

    def test_01_block_developer(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.admin))
        payload = {"reason": fake.text()}
        request = self.client.post(f"{self.url}{self.user.id}/block", payload, format="json")
        self.assertEqual(request.status_code, 201)

    def test_02_unblock_developer(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.admin))
        payload = {"reason": fake.text()}
        self.user.is_banned = True
        self.user.save()
        request = self.client.post(f"{self.url}{self.user.id}/unblock", payload, format="json")
        self.assertEqual(request.status_code, 201)

    def test_03_delete(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.admin))
        request = self.client.delete(f"{self.url}{self.user.id}/")
        self.assertEqual(request.status_code, 204)
