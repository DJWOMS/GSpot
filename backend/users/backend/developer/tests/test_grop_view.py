from base.base_tests.tests import BaseViewTestCase
from developer.models import CompanyUser, DeveloperPermission
from django.urls import reverse


class DeveloperGroupViewTest(BaseViewTestCase):
    @classmethod
    def setUpTestData(cls):
        cls.access_token = cls.create_access_token(cls)
        cls.url = '/api/v1/developer/group/'
        # cls.url = reverse('admin_group')
        permission = DeveloperPermission.objects.create(
            name=cls.faker.word(),
            codename=cls.faker.word(),
        )
        cls.data_for_creating_group = {
            "name": cls.faker.word(),
            "permission": [permission.pk],
        }

    def create_access_token(self):
        user = CompanyUser.objects.create(
            username=self.faker.word(),
            password=self.faker.word(),
            email=self.faker.email(),
            is_active=True,
        )
        return self.get_access_token(user)

    def test_01_get_group_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.access_token)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_02_get_group_not_authenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 403)

    def test_03_post_group_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.access_token)
        response = self.client.post(self.url, self.data_for_creating_group)
        self.assertEqual(response.status_code, 201)

    def test_04_post_group_not_authenticated(self):
        response = self.client.post(self.url, self.data_for_creating_group)
        self.assertEqual(response.status_code, 403)
