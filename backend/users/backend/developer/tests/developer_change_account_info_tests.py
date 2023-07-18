from base.base_tests.tests import BaseViewTestCase
from developer.models import CompanyUser
from django.urls import reverse


class DeveloperChangeAccountInfoApiTestCase(BaseViewTestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('developer-user-account')
        cls.admin_user = CompanyUser.objects.create(
            username='CompanyUser',
            email=cls.faker.email(),
            phone=cls.faker.random_number(digits=10, fix_len=True),
            is_active=True,
        )

    def setUp(self):
        super().setUp()

    def test_change_info_patch(self):
        self.client.force_authenticate(user=self.admin_user)
        url = self.url
        responce = self.client.get(url)
        self.assertEqual("CompanyUser", responce.data.get("username"))
        new_data = {
            "username": "CompanyUser2",
        }
        responce_change_username = self.client.put(url, data=new_data)
        self.assertEqual("CompanyUser2", responce_change_username.data.get("username"))

    def test_change_info_logout_user(self):
        url = self.url
        responce = self.client.get(url)
        self.assertEqual(403, responce.status_code)
