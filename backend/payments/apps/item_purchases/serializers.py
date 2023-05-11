from apps.base.fields import MoneyAmountSerializerField
from apps.base.serializer import PaymentServiceSerializer
from rest_framework import serializers


class ItemPaymentData(serializers.Serializer):
    owner_uuid = serializers.UUIDField()
    item_uuid = serializers.UUIDField()
    developer_uuid = serializers.UUIDField()
    price = MoneyAmountSerializerField()


class PurchaseItemsSerializer(PaymentServiceSerializer):
    user_uuid = serializers.UUIDField()
    items_payment_data = ItemPaymentData(many=True)
    return_url = serializers.URLField()
