import enum
from dataclasses import dataclass
from decimal import Decimal
from typing import NewType

from apps.payment_accounts.models import Account, BalanceChange
from apps.transactions.models import Invoice

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
