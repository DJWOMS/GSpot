from administrator.models import Admin
from base.base_tests.tests import BaseViewTestCase
from django.urls import reverse


class AdminChangeAccountInfoApiTestCase(BaseViewTestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('administrator-user-account')
        cls.admin_user = Admin.objects.create(
            username='Admin',
            email=cls.faker.email(),
            phone=cls.faker.random_number(digits=10, fix_len=True),
            is_active=True,
        )

    def setUp(self):
        super().setUp()

    def test_get_account_info(self):
        self.client.force_authenticate(user=self.admin_user)
        responce = self.client.get(self.url)
        self.assertEqual("Admin", responce.data.get("username"))

    def test_change_info_authorized(self):
        self.client.force_authenticate(user=self.admin_user)
        new_data = {
            "username": "Admin2",
        }
        responce_change_username = self.client.put(self.url, data=new_data)
        self.assertEqual("Admin2", responce_change_username.data.get("username"))

    def test_change_info_unauthorized(self):
        responce = self.client.get(self.url)
        self.assertEqual(403, responce.status_code)
