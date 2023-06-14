from django.test import TestCase
from utils.db.redis_client import RedisAccessClient, RedisRefreshClient, RedisTotpClient


class RedisClientTestCase(TestCase):
    def setUp(self) -> None:
        self.redis_access_client = RedisAccessClient()
        self.redis_refresh_client = RedisRefreshClient()
        self.redis_totp_client = RedisTotpClient()
        self.redis_access_client_basik = RedisAccessClient(3)
        self.redis_refresh_client_basik = RedisRefreshClient(3)
        self.redis_totp_client_basik = RedisTotpClient(3)

    def test_add_AccessToken(self):
        self.redis_access_client.add_token(token='test_access_token_one')
        result = self.redis_access_client.is_token_exist(token='test_access_token_one')
        self.assertEqual(bool(result), True)

    def test_is_token_exist_false(self):
        result = self.redis_access_client.is_token_exist(token='this_token_false')
        self.assertEqual(bool(result), False)

    def test_add_RefreshToken(self):
        self.redis_refresh_client.add_token(token='test_refresh_token_one')
        result = self.redis_refresh_client.is_token_exist(token='test_refresh_token_one')
        self.assertEqual(bool(result), True)

    def test_refresh_in_access(self):
        result_access = self.redis_access_client.is_token_exist(token='refresh:test_refresh_token_one', prefix=False)
        result_refresh = self.redis_refresh_client.is_token_exist(token='access:test_access_token_one', prefix=False)
        self.assertEqual(bool(result_access), False)
        self.assertEqual(bool(result_refresh), False)

    def test_add_TotpToken(self):
        self.redis_totp_client.add_token(token='test_totp_token_one')
        result = self.redis_totp_client.is_token_exist(token='test_totp_token_one')
        self.assertEqual(bool(result), True)

    def test_is_token_exist_TotpToken(self):
        result_access = self.redis_access_client.is_token_exist(token='totp:test_totp_token_one', prefix=False)
        result_refresh = self.redis_refresh_client.is_token_exist(token='totp:test_totp_token_one', prefix=False)
        result_totp = self.redis_totp_client.is_token_exist(token='wrong_totp_token')

        self.assertEqual(bool(result_refresh), False)
        self.assertEqual(bool(result_access), False)
        self.assertEqual(bool(result_totp), False)

    def test_all_tokens_in_one_db(self):
        self.redis_access_client_basik.add_token(token='access_one')
        self.redis_refresh_client.add_token(token='refresh_one')
        self.redis_totp_client.add_token(token='totp_one')
        result_access = self.redis_totp_client_basik.is_token_exist(token='access:access_one', prefix=False)
        result_refresh = self.redis_access_client_basik.is_token_exist(token='refresh:refresh_one', prefix=False)
        result_totp = self.redis_refresh_client_basik.is_token_exist(token='totp:totp_one', prefix=False)

        self.assertEqual(bool(result_access), True)
        self.assertEqual(bool(result_refresh), True)
        self.assertEqual(bool(result_totp), True)
