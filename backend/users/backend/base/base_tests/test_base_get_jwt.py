import time
from django.urls import reverse
import os
from common.services.jwt.token import Token


class GetJwtApiTestCase:
    def setUp(self):
        self.user = self.get_user_model()
        self.data = self.set_settings_user()
        self.first_user = self.user.objects.create(**self.data)
        self.first_user.is_active = True
        self.first_user.save()
        self.client.force_authenticate(user=self.first_user)
        self.url = reverse('get_jwt')
        self.user_data = {
            'user_id': str(self.first_user.id),
            'role': self.first_user._meta.app_label,
        }
        self.token = Token().generate_tokens(data=self.user_data)
        self.data = {'refresh_token': self.token.get('refresh')}

    @staticmethod
    def set_settings_user():
        raise NotImplementedError

    @staticmethod
    def get_user_model():
        raise NotImplementedError

    def client_post(self, data):
        return self.client.post(self.url, data=data, format='json')

    def test_correct_get_jwt(self):
        response = self.client_post(self.data)
        self.assertEqual(response.status_code, 200)
        decod_refresh_token = Token()._decode(response.data['refresh'])
        decod_refresh_token = {
            'user_id': decod_refresh_token['user_id'],
            'role': decod_refresh_token['role'],
        }
        self.assertEqual(decod_refresh_token, self.user_data)

    def test_wrong_post_refresh_token(self):
        data = {'refresh_token': self.token.get('refresh') + 'asd'}
        response = self.client_post(data)
        self.assertEqual(response.status_code, 401)

    def test_is_not_active_user(self):
        self.first_user.is_active = False
        response = self.client_post(self.data)
        self.assertEqual(response.status_code, 401)

    def test_expired_refresh_token(self):
        os.environ['REFRESH_TOKEN_ROTATE_MIN_LIFETIME'] = '87000'
        time.sleep(1)
        response = self.client_post(self.data)
        self.assertIsNot(self.data.get('refresh_token'), response.data['refresh'])
