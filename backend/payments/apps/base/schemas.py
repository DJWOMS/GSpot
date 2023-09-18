import enum
from dataclasses import dataclass
from decimal import Decimal
from typing import NewType

from apps.item_purchases.models import Invoice
from apps.payment_accounts.models import Account, BalanceChange
from django.conf import settings

URL = NewType('URLField', str)


class PaymentServices(enum.Enum):
    yookassa = 'yookassa'
    from_balance = 'from_balance'


class PaymentTypes(enum.Enum):
    bank_card = 'bank_card'
    yoo_money = 'yoo_money'
    sberbank = 'sberbank'
    qiwi = 'qiwi'
    from_balance = 'from_balance'


@dataclass(kw_only=True)
class PaymentServiceInfo:
    payment_service: PaymentServices
    payment_type: PaymentTypes | None = None


@dataclass
class ResponseParsedData:
    income_amount: Decimal
    account: Account
    balance_object: BalanceChange
    invoice: Invoice | None = None


EnumCurrencies = enum.Enum(
    'Currencies',
    {currency: currency for currency in settings.SUPPORTED_CURRENCIES},
)


@dataclass
class MoneyDataClass:
    amount: Decimal
    currency: EnumCurrencies


@dataclass
class YookassaMoneyDataClass:
    value: Decimal
    currency: EnumCurrencies = settings.DEFAULT_CURRENCY
