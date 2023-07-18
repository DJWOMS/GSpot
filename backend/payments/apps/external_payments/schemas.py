import enum
from uuid import UUID

from apps.base.schemas import URL, PaymentTypes, YookassaMoneyDataClass
from apps.base.classes import DRFtoDataClassMixin
from apps.payment_accounts.models import PayoutData
from pydantic import BaseModel, Field


class YookassaPaymentStatuses(enum.Enum):
    succeeded = 'payment.succeeded'
    canceled = 'payment.canceled'
    waiting_for_capture = 'payment.waiting_for_capture'
    refund_succeeded = 'refund.succeeded'
    payout_succeeded = 'succeeded'


# RESPONSE PAYMENT SCHEMAS
class PaymentMethodDataResponse(BaseModel):
    type_: PaymentTypes


class YookassaPaymentBody(BaseModel, DRFtoDataClassMixin):
    id_: UUID = Field(alias='id')
    income_amount: YookassaMoneyDataClass
    amount: YookassaMoneyDataClass
    description: str
    metadata: dict
    payment_method: PaymentMethodDataResponse

    class Config:
        allow_population_by_field_name = True


class YookassaPaymentResponse(BaseModel, DRFtoDataClassMixin):
    event: YookassaPaymentStatuses
    object_: YookassaPaymentBody = Field(alias='object',)

    class Config:
        allow_population_by_field_name = True


# CREATE PAYMENT SCHEMAS
class ConfirmationDataClass(BaseModel, DRFtoDataClassMixin):
    confirmation_type: str = Field(..., alias='type')
    return_url: URL

    class Config:
        allow_population_by_field_name = True


class PaymentMethodDataCreate(BaseModel, DRFtoDataClassMixin):
    payment_type: PaymentTypes = Field(..., alias='type')

    class Config:
        allow_population_by_field_name = True


class YookassaPaymentCreate(BaseModel, DRFtoDataClassMixin):
    amount: YookassaMoneyDataClass
    payment_method_data: PaymentMethodDataCreate
    confirmation: ConfirmationDataClass
    metadata: dict
    capture: bool = True
    refundable: bool = False
    description: str | None = None


class PayoutDestination(BaseModel):
    type_: PayoutData.PayoutType = Field(
        alias='type',
    )
    account_number: str

    class Config:
        allow_population_by_field_name = True


class YookassaPayoutModel(BaseModel):
    amount: YookassaMoneyDataClass
    payout_destination_data: PayoutDestination
    user_uuid: UUID
