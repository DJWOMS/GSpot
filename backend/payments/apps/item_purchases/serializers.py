from apps.base.fields import MoneyAmountSerializerField
from apps.base.schemas import EnumCurrencies
from apps.base.serializer import PaymentServiceSerializer
from rest_enumfield import EnumField
from rest_framework import serializers


class ItemPaymentData(serializers.Serializer):
    item_uuid = serializers.UUIDField()
    developer_uuid = serializers.UUIDField()
    price = MoneyAmountSerializerField()


class PurchaseItemsSerializer(PaymentServiceSerializer):
    user_uuid_from = serializers.UUIDField()
    user_uuid_to = serializers.UUIDField()
    items_payment_data = ItemPaymentData(many=True)
    return_url = serializers.URLField()
    price_with_commission = MoneyAmountSerializerField()
    currency = EnumField(choices=EnumCurrencies)


class RefundSerializer(serializers.Serializer):
    user_uuid = serializers.UUIDField()
    offer_uuid = serializers.UUIDField()
