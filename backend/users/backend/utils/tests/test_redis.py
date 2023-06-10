from django.test import TestCase
from utils.db.redis_validate import RedisValidateToken

from utils.db.redis_client import RedisAccessClient, RedisRefreshClient, RedisTotpClient


class RedisClientTestCase(TestCase):
    def setUp(self) -> None:
        self.redis_validator = RedisValidateToken()
        self.redis_access_client = RedisAccessClient()
        self.redis_refresh_client = RedisRefreshClient()
        self.redis_totp_client = RedisTotpClient()

    def test_add_AccessToken(self):
        self.redis_validator.add_token(client=self.redis_access_client,
                                       token='test_access_token_one',
                                       ttl=180,
                                       prefix=True)
        result = self.redis_validator.is_token_exist(client=self.redis_access_client,
                                                     token='access:test_access_token_one')
        self.assertEqual(result, True)

    def test_is_token_exist_false(self):
        result = self.redis_validator.is_token_exist(client=self.redis_access_client, token='this_token_false')
        self.assertEqual(result, False)

    def test_add_RefreshToken(self):
        self.redis_validator.add_token(client=self.redis_refresh_client,
                                       token='test_refresh_token_one',
                                       ttl=180,
                                       prefix=True)
        result = self.redis_validator.is_token_exist(client=self.redis_refresh_client,
                                                     token='refresh:test_refresh_token_one')
        self.assertEqual(result, True)

    def test_refresh_in_access(self):
        result_access = self.redis_validator.is_token_exist(client=self.redis_access_client,
                                                            token='refresh:test_refresh_token_one')
        result_refresh = self.redis_validator.is_token_exist(client=self.redis_refresh_client,
                                                             token='access:test_access_token_one')
        self.assertEqual(result_access, False)
        self.assertEqual(result_refresh, False)

    def test_add_TotpToken(self):
        self.redis_validator.add_token(client=self.redis_totp_client,
                                       token='test_totp_token_one',
                                       ttl=180,
                                       prefix=True)
        result = self.redis_validator.is_token_exist(client=self.redis_totp_client,
                                                     token='totp:test_totp_token_one')
        self.assertEqual(result, True)

    def test_is_token_exist_TotpToken(self):
        result_access = self.redis_validator.is_token_exist(client=self.redis_access_client,
                                                            token='totp:test_totp_token_one')
        result_refresh = self.redis_validator.is_token_exist(client=self.redis_refresh_client,
                                                             token='totp:test_totp_token_one')
        result_totp = self.redis_validator.is_token_exist(client=self.redis_totp_client,
                                                          token='wrong_totp_token')
        self.assertEqual(result_refresh, False)
        self.assertEqual(result_access, False)
        self.assertEqual(result_totp, False)
