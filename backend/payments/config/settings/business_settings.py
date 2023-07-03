from datetime import timedelta
from decimal import Decimal

from pydantic import BaseSettings
from yookassa import Configuration

MAX_BALANCE_DIGITS = 11
DEFAULT_CURRENCY = 'RUB'
SUPPORTED_CURRENCIES = (DEFAULT_CURRENCY,)
CURRENCIES = (*SUPPORTED_CURRENCIES, 'USD', 'EUR')
MAX_COMMISSION_VALUE = Decimal(100)
PERIOD_FOR_MYSELF_TASK = timedelta(seconds=10)
PERIOD_FOR_GIFT_TASK = timedelta(seconds=10)
MINIMUM_PAYOUT_AMOUNT = Decimal(500)
MAXIMUM_YOOKASSA_PAYOUT = Decimal(500000)
MAXIMUM_PAYOUTS_PER_MONTH = 1
MINUTES_FOR_INVOICE_ATTEMPTS = 60
INVOICE_ATTEMPTS_PER_PERIOD = 5


class YookassaConfig(BaseSettings):
    SHOP_ACCOUNT_ID: int
    SHOP_SECRET_KEY: str
    GATE_AWAY_ACCOUNT_ID: int
    GATE_AWAY_SECRET_KEY: str

    def get_payment_settings(self):
        Configuration.account_id = self.SHOP_ACCOUNT_ID
        Configuration.secret_key = self.SHOP_SECRET_KEY

    def get_payout_settings(self):
        Configuration.account_id = self.GATE_AWAY_ACCOUNT_ID
        Configuration.secret_key = self.GATE_AWAY_SECRET_KEY


YOOKASSA_CONFIG = YookassaConfig()
