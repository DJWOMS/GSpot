from datetime import timedelta
from decimal import Decimal

from pydantic import BaseSettings
from yookassa import Configuration

DEFAULT_CURRENCY = 'RUB'
CURRENCIES = ('RUB', 'USD', 'EUR')
MAX_BALANCE_DIGITS = 11
MAX_COMMISSION_VALUE = Decimal(100)
PERIOD_FOR_MYSELF_TASK = timedelta(days=1)
PERIOD_FOR_GIFT_TASK = timedelta(days=7)


class YookassaConfig(BaseSettings):
    SHOP_ACCOUNT_ID: int
    SHOP_SECRET_KEY: str

    @property
    def payment(self):
        Configuration.account_id = self.SHOP_ACCOUNT_ID
        Configuration.secret_key = self.SHOP_SECRET_KEY


yookassa_config = YookassaConfig()
