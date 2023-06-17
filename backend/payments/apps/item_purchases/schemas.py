from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID

from apps.base.schemas import URL, MoneyDataClass, PaymentServiceInfo


@dataclass
class ItemPaymentData:
    item_uuid: UUID
    price: MoneyDataClass
    developer_uuid: UUID


@dataclass(kw_only=True)
class PurchaseItemsData(PaymentServiceInfo):
    user_uuid_from: UUID
    user_uuid_to: UUID
    return_url: URL
    items_payment_data: list[ItemPaymentData]
    price_with_commission: MoneyDataClass

    def items_total_price(self) -> Decimal:
        return sum(item_payment_data.price.amount for item_payment_data in self.items_payment_data)


@dataclass
class ItemPurchaseData:
    user_uuid: UUID
    item_uuid: UUID
