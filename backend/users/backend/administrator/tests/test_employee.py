from administrator.models import Admin
from base.base_tests.tests import BaseTestView
from common.models import Country
from django.urls import reverse


class EmployeeViewTest(BaseTestView):
    fixtures = ['fixtures/message_and_notify']

    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('admin_employee')
        Country.objects.create(id=1, name=cls.faker.country())
        cls.valid_admin = Admin.objects.create_superuser(
            username=cls.faker.first_name(),
            email=cls.faker.email(),
            password=cls.faker.word(),
            phone=cls.faker.random_number(digits=10, fix_len=True),
        )
        cls.invalid_admin = Admin.objects.create_user(
            username=cls.faker.first_name(),
            email=cls.faker.email(),
            password=cls.faker.word(),
            phone=cls.faker.random_number(digits=10, fix_len=True),
        )
        cls.employee = Admin.objects.create_user(
            username=cls.faker.first_name(),
            email=cls.faker.email(),
            password=cls.faker.word(),
            phone=cls.faker.random_number(digits=10, fix_len=True),
        )
        cls.test_data = {
            "username": cls.faker.word(),
            "first_name": cls.faker.first_name(),
            "last_name": cls.faker.last_name(),
            "email": cls.faker.email(),
            "phone": cls.faker.random_number(digits=10, fix_len=True),
            "country": 1,
            "is_banned": False,
        }

    def test_000_create_employee(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.valid_admin))
        request = self.client.post(self.url, self.test_data)
        self.assertEqual(request.status_code, 201)

    def test_01_create_not_authorized_user(self):
        request = self.client.post(self.url, self.test_data)
        self.assertEqual(request.status_code, 403)

    def test_02_permissions(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.valid_admin))
        request = self.client.get(self.url)
        self.assertEqual(request.status_code, 200)
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.invalid_admin))
        request = self.client.get(self.url)
        self.assertEqual(request.status_code, 403)

    def test_03_get_retrieve(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.valid_admin))
        request = self.client.get(f"{self.url}{self.employee.id}/")
        self.assertEqual(request.status_code, 200)

    def test_04_partial_update(self):
        data = {"last_name": self.faker.word()}
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.valid_admin))
        request = self.client.put(f"{self.url}{self.employee.id}/", data)
        self.assertEqual(request.status_code, 200)
        self.assertEqual(Admin.objects.get(pk=self.employee.id).last_name, data["last_name"])

    def test_05_delete(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.get_token(self.valid_admin))
        request = self.client.delete(f"{self.url}{self.employee.id}/")
        self.assertEqual(request.status_code, 204)
