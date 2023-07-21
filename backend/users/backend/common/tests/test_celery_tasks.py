import datetime
from unittest.mock import patch

from common.tasks import create_payment_account
from customer.models import CustomerUser
from django.conf import settings
from rest_framework.test import APITestCase


class DeveloperAuthViewTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.customer: CustomerUser = CustomerUser.objects.create_user(
            username="test_user",
            email="email@mail.ru",
            password="test_user1",
            first_name="user_test_name",
            last_name="user_test_name",
            phone="89991234567",
            is_active=True,
            birthday=datetime.date.today(),
        )

    @patch("common.tasks.requests.post")
    def test_000_create_payment_account(self, mock_post):
        mock_post.return_value.status_code = 201
        create_payment_account(user_uuid=self.customer.id)
        mock_post.assert_called_once_with(
            f"{settings.PAYMENTS_DOMAIN}/api/v1/payment_accounts/create_account/",
            data={"user_uuid": self.customer.id},
        )
