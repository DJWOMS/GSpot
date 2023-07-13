from administrator.models import Admin
from base.base_tests.tests import BaseTestView
from base.models import BaseAbstractUser
from django.urls import reverse


class AdminChangeAccountInfoApiTestCase(BaseTestView):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('administrator-user-account')
        cls.admin_user = cls.create_user(Admin, username='Admin')

    @classmethod
    def create_user(cls, model: type[BaseAbstractUser], **kwargs) -> type[BaseAbstractUser]:
        data = {
            "email": cls.faker.email(),
            "phone": cls.faker.random_number(digits=10, fix_len=True),
            "is_active": True,
        }
        return model.objects.create(**data, **kwargs)

    def setUp(self):
        super().setUp()

    def test_change_info_patch(self):
        self.client.force_authenticate(user=self.admin_user)
        url = self.url
        responce = self.client.get(url)
        self.assertEqual("Admin", responce.data.get("username"))
        new_data = {
            "username": "Admin2",
        }
        responce_change_username = self.client.put(url, data=new_data)
        self.assertEqual("Admin2", responce_change_username.data.get("username"))

    def test_change_info_logout_user(self):
        url = self.url
        responce = self.client.get(url)
        self.assertEqual(403, responce.status_code)
