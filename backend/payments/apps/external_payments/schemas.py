import enum
from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID

from django.conf import settings


class PaymentResponseStatuses(enum.Enum):
    succeeded = 'payment.succeeded'
    canceled = 'payment.canceled'
    waiting_for_capture = 'payment.waiting_for_capture'
    refund_succeeded = 'refund.succeeded'


class YookassaPaymentTypes(enum.Enum):
    bank_card = 'bank_card'
    yoo_money = 'yoo_money'
    sberbank = 'sberbank'
    qiwi = 'qiwi'


@dataclass
class AmountDataClass:
    value: Decimal
    currency: str = settings.DEFAULT_CURRENCY


@dataclass
class YookassaPaymentResponseObject:
    id: UUID
    income_amount: AmountDataClass
    description: str
    metadata: dict


@dataclass
class YookassaPaymentResponse:
    event: PaymentResponseStatuses
    object: YookassaPaymentResponseObject


@dataclass
class PaymentMethodData:
    type: YookassaPaymentTypes


@dataclass
class ConfirmationDataClass:
    type: str
    return_url: str


@dataclass
class YookassaPaymentCreate:
    amount: AmountDataClass
    payment_method_data: PaymentMethodData
    confirmation: ConfirmationDataClass
    metadata: dict
    capture: bool = True
    refundable: bool = False
    description: str | None = None


class PaymentTypes(enum.Enum):
    from_balance = 'from_balance'
    yookassa_payments: YookassaPaymentTypes


@dataclass
class YookassaPaymentInfo:
    payment_type: PaymentTypes
    payment_amount: Decimal


@dataclass
class PaymentCreateDataClass(YookassaPaymentInfo):
    user_uuid: UUID
    return_url: str
