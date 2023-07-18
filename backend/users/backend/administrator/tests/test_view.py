from administrator.models import Admin
from base.base_tests.tests import BaseViewTestCase


class AdminPermissionViewTest(BaseViewTestCase):
    @classmethod
    def setUpTestData(cls):
        cls.access_token = cls.create_access_token(cls)
        cls.url = '/api/v1/admin/permission/'
        cls.creating_permission_data = {
            "name": cls.faker.word(),
            "codename": cls.faker.word(),
        }

    def create_access_token(self):
        user = Admin.objects.create(
            username=self.faker.word(),
            password=self.faker.word(),
            email=self.faker.email(),
        )
        return self.get_access_token(user)

    def test_get_permission_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.access_token)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_get_permission_not_authenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 403)

    def test_post_permission_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.access_token)
        response = self.client.post(self.url, self.creating_permission_data)
        self.assertEqual(response.status_code, 201)

    def test_post_permission_not_authenticated(self):
        response = self.client.post(self.url, self.creating_permission_data)
        self.assertEqual(response.status_code, 403)
