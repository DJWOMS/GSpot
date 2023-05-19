from django.test import TestCase
from utils.db.redis_validate import RedisValidateToken

from utils.db.redis_client import RedisAccessClient, RedisRefreshClient


class RedisClientTestCase(TestCase):
    def setUp(self) -> None:
        self.redis_validator = RedisValidateToken()
        self.redis_access_client = RedisAccessClient()
        self.redis_refresh_client = RedisRefreshClient()

    def test_add_AccessToken(self):
        self.redis_validator.add_token(client=self.redis_access_client,
                                       token='test_access_token_one',
                                       ttl=180,
                                       prefix='access')
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
                                       prefix='refresh')
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
