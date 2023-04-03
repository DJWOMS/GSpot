from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID

from apps.external_payments.schemas import PaymentTypes


@dataclass
class ItemPaymentData:
    owner_id: UUID
    item_uuid: UUID
    price: Decimal


@dataclass
class IncomeData:
    user_uuid: UUID
    payment_type: PaymentTypes
    items_payment_data: list[ItemPaymentData]
    return_url: str
