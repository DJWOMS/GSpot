from administrator.models import Admin
from base.base_tests.tests import BaseTestView
from common.models import Country
from customer.models import CustomerUser
from django.urls import reverse


class CustomersViewTest(BaseTestView):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse("admin_customers")
        Country.objects.create(id=1, name=cls.faker.country())
        cls.admin = Admin.objects.create_superuser(
            username=cls.faker.first_name(),
            email=cls.faker.email(),
            password=cls.faker.word(),
            phone=cls.faker.random_number(digits=10, fix_len=True),
        )
        cls.user = CustomerUser.objects.create_user(
            username=cls.faker.word(),
            email=cls.faker.email(),
            password=cls.faker.word(),
            first_name=cls.faker.first_name(),
            last_name=cls.faker.last_name(),
            phone=cls.faker.random_number(digits=10, fix_len=True),
            birthday=cls.faker.date_object(),
        )

    def test_000_list_customer(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.admin))
        request = self.client.get(self.url)
        self.assertEqual(request.status_code, 200)

    def test_01_block_customer(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.admin))
        payload = {"reason": self.faker.text()}
        request = self.client.post(f"{self.url}{self.user.id}/block", payload, format="json")
        self.assertEqual(request.status_code, 201)

    def test_02_unblock_customer(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.admin))
        payload = {"reason": self.faker.text()}
        self.user.is_banned = True
        self.user.save()
        request = self.client.post(f"{self.url}{self.user.id}/unblock", payload, format="json")
        self.assertEqual(request.status_code, 201)

    def test_03_delete(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.admin))
        request = self.client.delete(f"{self.url}{self.user.id}/")
        self.assertEqual(request.status_code, 204)
