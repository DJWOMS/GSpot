from unittest.mock import patch

from administrator.models import Admin
from base.base_tests.tests import BaseViewTestCase
from base.models import BaseAbstractUser
from common.services.totp import TOTPToken
from config.settings import redis_config
from customer.models import CustomerUser
from developer.models import CompanyUser
from utils.db.redis_client import RedisTotpClient


class TestTOTPToken(BaseViewTestCase):
    fixtures = ['fixtures/message_and_notify']

    @classmethod
    def setUpTestData(cls):
        cls.totp = TOTPToken()
        cls.developer = cls.create_user(CompanyUser)
        cls.administrator = cls.create_user(Admin)
        cls.customer = cls.create_user(CustomerUser)

    @classmethod
    def create_user(cls, user_model: type[BaseAbstractUser]) -> type[BaseAbstractUser]:
        data = {
            "username": cls.faker.word(),
            "password": cls.faker.word(),
            "email": cls.faker.email(),
            "phone": cls.faker.random_number(digits=10, fix_len=True),
        }
        if user_model == CustomerUser:
            data["birthday"] = cls.faker.date_object()
        return user_model.objects.create_user(**data)

    def setUp(self):
        self.r = RedisTotpClient(
            host=redis_config.REDIS_LOCAL_HOST,
            port=redis_config.REDIS_LOCAL_PORT,
            db=redis_config.REDIS_TOTP_DB,
            password=redis_config.REDIS_LOCAL_PASSWORD,
        )

    @patch("common.services.totp.totp.TOTPToken.generate_totp")
    def test_totp_for_developer(self, mock_generate_totp):
        test_token = self.totp.generate_totp()
        mock_generate_totp.return_value = test_token
        self.totp.send_totp(self.developer)

        encoded_data = self.r.is_token_exist(test_token)
        data = {key: value for key, value in encoded_data.items()}
        self.assertEqual(data["user_id"], str(self.developer.id))
        self.assertEqual(data["role"], self.developer._meta.app_label)

    @patch("common.services.totp.totp.TOTPToken.generate_totp")
    def test_totp_for_admin(self, mock_generate_totp):
        test_token = self.totp.generate_totp()
        mock_generate_totp.return_value = test_token
        self.totp.send_totp(self.administrator)

        encoded_data = self.r.is_token_exist(test_token)
        data = {key: value for key, value in encoded_data.items()}
        self.assertEqual(data["user_id"], str(self.administrator.id))
        self.assertEqual(data["role"], self.administrator._meta.app_label)

    @patch("common.services.totp.totp.TOTPToken.generate_totp")
    def test_totp_for_customer(self, mock_generate_totp):
        test_token = self.totp.generate_totp()
        mock_generate_totp.return_value = test_token
        self.totp.send_totp(self.customer)

        encoded_data = self.r.is_token_exist(test_token)
        data = {key: value for key, value in encoded_data.items()}
        self.assertEqual(data["user_id"], str(self.customer.id))
        self.assertEqual(data["role"], self.customer._meta.app_label)
