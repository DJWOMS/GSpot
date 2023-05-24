from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID

from apps.base.schemas import URL, EnumCurrencies, PaymentServiceInfo


@dataclass
class ItemPaymentData:
    item_uuid: UUID
    price: Decimal
    developer_uuid: UUID


@dataclass(kw_only=True)
class PurchaseItemsData(PaymentServiceInfo):
    user_uuid_from: UUID
    user_uuid_to: UUID
    return_url: URL
    items_payment_data: list[ItemPaymentData]
    price_with_commission: Decimal
    currency: EnumCurrencies

    def items_total_price(self) -> Decimal:
        return sum(item_payment_data.price for item_payment_data in self.items_payment_data)


@dataclass
class RefundData:
    user_uuid: UUID
    offer_uuid: UUID
