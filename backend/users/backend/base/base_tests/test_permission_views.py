from rest_framework.test import APIClient

from base.models import BaseAbstractUser
from common.services.jwt.token import Token


class BasePermissionViewsTest:
    def setUp(self):
        self.client = APIClient()
        self.access_token = self.create_access_token()
        self.path = self.get_permission_path()
        self.data_for_creating_permission = {
            'name': 'test_name',
            'codename': 'test_codename',
        }

    def create_access_token(self):
        user_model = self.get_user_model()
        user = user_model.objects.create(
            username='test_user', password='test_password', email='test_email@example.com'
        )
        user_data = {'user_id': str(user.id), 'role': user_model._meta.app_label}
        return Token().generate_access_token(user_data)

    @staticmethod
    def get_user_model() -> BaseAbstractUser:
        raise NotImplementedError

    @staticmethod
    def get_permission_path() -> str:
        raise NotImplementedError

    def test_get_permission_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.access_token)
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 200)

    def test_get_permission_not_authenticated(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 403)

    def test_post_permission_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.access_token)
        response = self.client.post(self.path, self.data_for_creating_permission)
        self.assertEqual(response.status_code, 201)

    def test_post_permission_not_authenticated(self):
        response = self.client.post(self.path, self.data_for_creating_permission)
        self.assertEqual(response.status_code, 403)
