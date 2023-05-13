from django.test import TestCase
from rest_framework.test import APIClient

from common.services.jwt.token import Token


class TestJWTLogoutView(TestCase):
    def setUp(self):
        token = Token()
        self.path = "/api/users/logout/"
        self.client = APIClient()
        self.valid_token = {"refresh_token": token.generate_refresh_token()}
        self.invalid_token = {"refresh_token": "testinvalidrefreshtoken"}

    def test_logout_with_valid_token(self):
        response = self.client.post(self.path, self.valid_token, format='json')
        self.assertEqual(response.status_code, 205)

    def test_logout_with_invalid_token(self):
        response = self.client.post(self.path, self.invalid_token, format='json')
        self.assertEqual(response.status_code, 400)

    def test_logout_without_token(self):
        response = self.client.post(self.path)
        self.assertEqual(response.status_code, 400)
