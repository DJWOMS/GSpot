import os
import time

from administrator.models import Admin
from base.base_tests.tests import BaseViewTestCase
from common.services.jwt.token import Token
from django.urls import reverse


class AdminGetJwtApiTestCase(BaseViewTestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = Admin.objects.create_user(
            username=cls.faker.word(),
            email=cls.faker.email(),
            password=cls.faker.word(),
            first_name=cls.faker.first_name(),
            last_name=cls.faker.last_name(),
            phone=cls.faker.random_number(digits=10, fix_len=True),
            is_active=True,
        )
        cls.url = reverse("token_refresh")
        cls.token = cls.get_tokens(cls.user)
        cls.data = {"refresh_token": cls.token.get("refresh")}

    def client_post(self, data):
        return self.client.post(self.url, data=data, format="json")

    def test_000_correct_get_jwt(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.token.get('access'))
        response = self.client_post(self.data)
        self.assertEqual(response.status_code, 200)
        decoded_refresh_token = Token()._decode(response.data["refresh"])
        decoded_refresh_token = {
            "user_id": decoded_refresh_token["user_id"],
            "role": decoded_refresh_token["role"],
        }
        self.assertEqual(
            decoded_refresh_token,
            {"user_id": str(self.user.id), "role": self.user._meta.app_label},
        )

    def test_01_wrong_post_refresh_token(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.token.get('access'))
        data = {"refresh_token": self.token.get("refresh") + "asd"}
        response = self.client_post(data)
        self.assertEqual(response.status_code, 401)

    def test_02_is_not_active_user(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.token.get('access'))
        self.user.is_active = False
        self.user.save()
        response = self.client_post(self.data)
        self.assertEqual(response.status_code, 401)

    def test_03_expired_refresh_token(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.token.get('access'))
        os.environ["REFRESH_TOKEN_ROTATE_MIN_LIFETIME"] = "87000"
        time.sleep(1)
        response = self.client_post(self.data)
        self.assertIsNot(self.data.get("refresh_token"), response.data["refresh"])

    def test_04_ban_list_refresh_token(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.token.get('access'))
        refresh_token = self.data['refresh_token']
        self.assertEqual(Token().get_refresh_data(refresh_token), None)
        Token().add_refresh_to_redis(token=refresh_token)
        response = self.client_post(self.data)
        self.assertEqual(response.status_code, 401)
