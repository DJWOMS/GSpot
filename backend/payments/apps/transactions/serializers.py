from rest_framework import serializers

from apps.base.fields import MoneySerializerField
from apps.base.serializer import PaymentServiceSerializer


class ItemPaymentData(serializers.Serializer):
    owner_uuid = serializers.UUIDField()
    item_uuid = serializers.UUIDField()
    developer_uuid = serializers.UUIDField()
    price = MoneySerializerField()


class PurchaseItemsSerializer(PaymentServiceSerializer):
    user_uuid = serializers.UUIDField()
    items_payment_data = ItemPaymentData(many=True)
    return_url = serializers.URLField()
