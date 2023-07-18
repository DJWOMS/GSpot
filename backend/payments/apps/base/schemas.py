import enum
from decimal import Decimal
from typing import NewType, Optional
from pydantic import BaseModel

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


class PaymentServiceInfo(BaseModel):
    payment_service: PaymentServices
    payment_type: Optional[PaymentTypes] = None


class ResponseParsedData(BaseModel):
    income_amount: Decimal
    account: Account
    balance_object: BalanceChange
    invoice: Optional[Invoice] = None

    class Config:
        arbitrary_types_allowed = True


EnumCurrencies = enum.Enum(
    'Currencies',
    {currency: currency for currency in settings.SUPPORTED_CURRENCIES},
)


class MoneyDataClass(BaseModel):
    amount: Decimal
    currency: EnumCurrencies


class YookassaMoneyDataClass(BaseModel):
    value: Decimal
    currency: EnumCurrencies = settings.DEFAULT_CURRENCY
