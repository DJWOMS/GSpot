from administrator.models import Admin, AdminPermission
from base.base_tests.tests import BaseViewTestCase
from django.urls import reverse


class AdminGroupViewTest(BaseViewTestCase):
    @classmethod
    def setUpTestData(cls):
        cls.access_token = cls.create_access_token(cls)
        cls.url = '/api/v1/admin/group/'
        permission = AdminPermission.objects.create(
            name=cls.faker.word(),
            codename=cls.faker.word(),
        )
        cls.data_for_creating_group = {
            "name": cls.faker.word(),
            "permission": [permission.pk],
        }

    def create_access_token(self):
        user = Admin.objects.create(
            username=self.faker.word(),
            password=self.faker.word(),
            email=self.faker.email(),
        )
        return self.get_access_token(user)

    def test_get_group_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.access_token)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_get_group_not_authenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 403)

    def test_post_group_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.access_token)
        response = self.client.post(self.url, self.data_for_creating_group)
        self.assertEqual(response.status_code, 201)

    def test_post_group_not_authenticated(self):
        response = self.client.post(self.url, self.data_for_creating_group)
        self.assertEqual(response.status_code, 403)
