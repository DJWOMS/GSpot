from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID

from apps.base.schemas import URL, PaymentServiceInfo


@dataclass
class ItemPaymentData:
    owner_uuid: UUID
    item_uuid: UUID
    price: Decimal
    developer_uuid: UUID


@dataclass(kw_only=True)
class PurchaseItemsData(PaymentServiceInfo):
    user_uuid: UUID
    return_url: URL
    items_payment_data: list[ItemPaymentData]

    def total_price(self):
        return sum(item_payment_data.price for item_payment_data in self.items_payment_data)
