from administrator.models import Admin
from base.base_tests.tests import BaseViewTestCase
from common.models import Country
from developer.models import CompanyUser
from django.urls import reverse


class DevelopersViewTest(BaseViewTestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse("admin_developers")
        Country.objects.create(id=1, name=cls.faker.country())
        cls.admin = Admin.objects.create_superuser(
            username=cls.faker.first_name(),
            email=cls.faker.email(),
            password=cls.faker.word(),
            phone=cls.faker.random_number(digits=10, fix_len=True),
        )
        cls.user = CompanyUser.objects.create_user(
            username=cls.faker.word(),
            email=cls.faker.email(),
            password=cls.faker.word(),
            first_name=cls.faker.first_name(),
            last_name=cls.faker.last_name(),
            phone=cls.faker.random_number(digits=10, fix_len=True),
        )

    def test_000_list_developer(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_access_token(self.admin))
        request = self.client.get(self.url)
        self.assertEqual(request.status_code, 200)

    def test_01_block_developer(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_access_token(self.admin))
        payload = {"reason": self.faker.text()}
        request = self.client.post(f"{self.url}{self.user.id}/block", payload, format="json")
        self.assertEqual(request.status_code, 201)

    def test_02_unblock_developer(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_access_token(self.admin))
        payload = {"reason": self.faker.text()}
        self.user.is_banned = True
        self.user.save()
        request = self.client.post(f"{self.url}{self.user.id}/unblock", payload, format="json")
        self.assertEqual(request.status_code, 201)

    def test_03_delete(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_access_token(self.admin))
        request = self.client.delete(f"{self.url}{self.user.id}/")
        self.assertEqual(request.status_code, 204)
