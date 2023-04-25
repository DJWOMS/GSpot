from datetime import timedelta
from decimal import Decimal

DEFAULT_CURRENCY = 'RUB'
MAX_BALANCE_DIGITS = 11
MAX_COMMISSION_VALUE = Decimal(100)
PERIOD_FOR_MYSELF_TASK = timedelta(days=1)
PERIOD_FOR_GIFT_TASK = timedelta(days=7)
