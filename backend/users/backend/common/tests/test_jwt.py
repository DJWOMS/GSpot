from datetime import datetime, timedelta
from typing import Type

from django.test import TestCase
from django.utils import timezone

from config.settings import redis_config
from administrator.models import Admin
from base.exceptions import UserBanned, UserInActive
from base.models import BaseAbstractUser
from common.services.jwt.exceptions import PayloadError, TokenInvalid, TokenExpired
from common.services.jwt.token import Token
from customer.models import CustomerUser
from developer.models import CompanyUser
from utils.db.redis_client import RedisAccessClient


class TestTokenJWT(TestCase):
    def setUp(self):
        self.token = Token()
        self.developer = self.create_user(CompanyUser)
        self.administrator = self.create_user(Admin)
        self.customer = self.create_user(CustomerUser)
        self.redis_access_client = RedisAccessClient(host=redis_config.REDIS_HOST,
                                                     port=redis_config.REDIS_PORT,
                                                     db=redis_config.REDIS_ACCESS_DB,
                                                     password=redis_config.REDIS_PASSWORD)

    @staticmethod
    def create_user(user_model: Type[BaseAbstractUser]) -> Type[BaseAbstractUser]:
        data = {
            'username': 'test_user',
            'password': 'test_password',
            'email': 'test_email@example.com',
            'phone': 12341234,
            'is_active': True,
        }
        if user_model == CustomerUser:
            data['birthday'] = datetime.now()
        user = user_model.objects.create_user(**data)
        return user

    @staticmethod
    def get_payload_for_user(user: Type[BaseAbstractUser]) -> dict:
        user_payload = {'user_id': str(user.id), 'role': user._meta.app_label}
        return user_payload

    def test_create_valid_payload_admin_tokens(self):
        user_payload = self.get_payload_for_user(self.administrator)
        tokens = self.token.generate_tokens(user_payload)
        self.assertIsInstance(tokens, dict)

    def test_create_valid_payload_developer_tokens(self):
        user_payload = self.get_payload_for_user(self.developer)
        tokens = self.token.generate_tokens(user_payload)
        self.assertIsInstance(tokens, dict)

    def test_create_valid_payload_customer_tokens(self):
        user_payload = self.get_payload_for_user(self.customer)
        tokens = self.token.generate_tokens(user_payload)
        self.assertIsInstance(tokens, dict)

    def test_create_empty_payload_tokens(self):
        user_payload = {}
        self.assertRaises(PayloadError, self.token.generate_tokens, user_payload)

    def test_create_empty_user_id_payload_tokens(self):
        user_payload = {'role': 'administrator'}
        self.assertRaises(PayloadError, self.token.generate_tokens, user_payload)

    def test_create_empty_role_payload_tokens(self):
        user_payload = {'user_id': 'test_user_id'}
        self.assertRaises(PayloadError, self.token.generate_tokens, user_payload)

    def test_create_tokens_for_admin_user(self):
        tokens = self.token.generate_tokens_for_user(self.administrator)
        self.assertIsInstance(tokens, dict)

    def test_create_tokens_for_developer_user(self):
        tokens = self.token.generate_tokens_for_user(self.developer)
        self.assertIsInstance(tokens, dict)

    def test_create_tokens_for_customer_user(self):
        tokens = self.token.generate_tokens_for_user(self.customer)
        self.assertIsInstance(tokens, dict)

    def test_create_tokens_for_inactive_admin_user(self):
        self.administrator.is_active = False
        self.assertRaises(UserInActive, self.token.generate_tokens_for_user, self.administrator)

    def test_create_tokens_for_inactive_developer_user(self):
        self.developer.is_active = False
        self.assertRaises(UserInActive, self.token.generate_tokens_for_user, self.developer)

    def test_create_tokens_for_inactive_customer_user(self):
        self.customer.is_active = False
        self.assertRaises(UserInActive, self.token.generate_tokens_for_user, self.customer)

    def test_create_tokens_for_banned_admin_user(self):
        self.administrator.is_banned = True
        self.assertRaises(UserBanned, self.token.generate_tokens_for_user, self.administrator)

    def test_create_tokens_for_banned_developer_user(self):
        self.developer.is_banned = True
        self.assertRaises(UserBanned, self.token.generate_tokens_for_user, self.developer)

    def test_create_tokens_for_banned_customer_user(self):
        self.customer.is_banned = True
        self.assertRaises(UserBanned, self.token.generate_tokens_for_user, self.customer)

    def test_check_valid_token_signature(self):
        user_payload = self.get_payload_for_user(self.administrator)
        tokens = self.token.generate_tokens(user_payload)
        access_token = tokens['access']
        self.assertIsNone(self.token.check_signature(access_token))

    def test_check_valid_token_exp(self):
        user_payload = self.get_payload_for_user(self.administrator)
        tokens = self.token.generate_tokens(user_payload)
        access_token = tokens['access']
        exp_left = self.token.check_exp(access_token)
        self.assertIsInstance(exp_left, int)

    def test_check_invalid_token_signature(self):
        invalid_token = 'invalid.jwt_token'
        self.assertRaises(TokenInvalid, self.token.check_signature, invalid_token)

    def test_check_expired_token(self):
        iat = timezone.localtime()
        expired_time = iat - timedelta(days=30)
        payload = {
            'exp': int(expired_time.timestamp()),
        }
        token = self.token._encode(payload)
        self.assertRaises(TokenExpired, self.token.check_exp, token)
