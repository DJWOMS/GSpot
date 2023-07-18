from decimal import Decimal
from uuid import UUID
from pydantic import BaseModel

from apps.base.schemas import URL, PaymentServiceInfo, YookassaMoneyDataClass


class CommissionCalculationInfo(PaymentServiceInfo, BaseModel):
    payment_amount: Decimal

    class Config:
        allow_population_by_field_name = True


class BalanceIncreaseData(PaymentServiceInfo, BaseModel):
    user_uuid: UUID
    return_url: URL
    amount: YookassaMoneyDataClass


class YookassaRequestPayment(BalanceIncreaseData, BaseModel):
    metadata: dict
