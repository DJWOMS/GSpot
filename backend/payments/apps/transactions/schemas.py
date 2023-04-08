from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID

from apps.base.schemas import URL
from apps.external_payments.schemas import PaymentTypes


@dataclass
class ItemPaymentData:
    owner_uuid: UUID
    item_uuid: UUID
    price: Decimal
    developer_uuid: UUID


@dataclass
class IncomeData:
    user_uuid: UUID
    payment_type: PaymentTypes
    items_payment_data: list[ItemPaymentData]
    return_url: URL

    def total_price(self):
        return sum(
            item_payment_data.price for item_payment_data
            in self.items_payment_data
        )
