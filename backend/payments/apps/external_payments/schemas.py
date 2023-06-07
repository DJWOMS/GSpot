import enum
from dataclasses import dataclass, field
from decimal import Decimal
from uuid import UUID

from apps.base.schemas import URL, EnumCurrencies, PaymentTypes
from apps.payment_accounts.models import PayoutData
from dataclasses_json import config, dataclass_json
from django.conf import settings
from pydantic import BaseModel, Field


class YookassaPaymentStatuses(enum.Enum):
    succeeded = 'payment.succeeded'
    canceled = 'payment.canceled'
    waiting_for_capture = 'payment.waiting_for_capture'
    refund_succeeded = 'refund.succeeded'
    payout_succeeded = 'succeeded'


@dataclass
class AmountDataClass:
    value: Decimal
    currency: str = settings.DEFAULT_CURRENCY


# RESPONSE PAYMENT SCHEMAS
@dataclass
class PaymentMethodDataResponse:
    type_: PaymentTypes


@dataclass_json
@dataclass
class YookassaPaymentBody:
    id_: UUID = field(metadata=config(field_name='id'))
    income_amount: AmountDataClass
    amount: AmountDataClass
    description: str
    metadata: dict
    payment_method: PaymentMethodDataResponse


@dataclass_json
@dataclass
class YookassaPaymentResponse:
    event: YookassaPaymentStatuses
    object_: YookassaPaymentBody = field(
        metadata=config(field_name='object'),
    )


# CREATE PAYMENT SCHEMAS
@dataclass_json
@dataclass
class ConfirmationDataClass:
    confirmation_type: str = field(metadata=config(field_name='type'))
    return_url: URL


@dataclass_json
@dataclass
class PaymentMethodDataCreate:
    payment_type: PaymentTypes = field(
        metadata=config(field_name='type'),
    )


@dataclass_json
@dataclass
class YookassaPaymentCreate:
    amount: AmountDataClass
    payment_method_data: PaymentMethodDataCreate
    confirmation: ConfirmationDataClass
    metadata: dict
    capture: bool = True
    refundable: bool = False
    description: str | None = None


class AmountModel(BaseModel):
    value: Decimal
    currency: EnumCurrencies = EnumCurrencies.RUB


class PayoutDestination(BaseModel):
    type_: PayoutData.PayoutType = Field(
        alias='type',
    )
    account_number: str

    class Config:
        allow_population_by_field_name = True


class YookassaPayoutModel(BaseModel):
    amount: AmountModel
    payout_destination_data: PayoutDestination
    user_uuid: UUID
