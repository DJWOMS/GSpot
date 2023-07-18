from decimal import Decimal
from uuid import UUID
from pydantic import BaseModel

from apps.base.schemas import URL, MoneyDataClass, PaymentServiceInfo


class ItemPaymentData(BaseModel):
    item_uuid: UUID
    price: MoneyDataClass
    developer_uuid: UUID


class PurchaseItemsData(PaymentServiceInfo, BaseModel):
    user_uuid_from: UUID
    user_uuid_to: UUID
    return_url: URL
    items_payment_data: list[ItemPaymentData]
    price_with_commission: MoneyDataClass

    def items_total_price(self) -> Decimal:
        return sum(item_payment_data.price.amount for item_payment_data in self.items_payment_data)


class ItemPurchaseData(BaseModel):
    user_uuid_from: UUID
    user_uuid_to: UUID
    item_uuid: UUID
