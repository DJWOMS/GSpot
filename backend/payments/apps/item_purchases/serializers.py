from apps.base.serializer import MoneySerializer, PaymentServiceSerializer
from rest_framework import serializers


class ItemPaymentData(serializers.Serializer):
    item_uuid = serializers.UUIDField()
    developer_uuid = serializers.UUIDField()
    price = MoneySerializer()

    def to_internal_value(self, data):
        if 'offer_uuid' in data.keys():
            data['item_uuid'] = data['offer_uuid']
            del data['offer_uuid']
        return super().to_internal_value(data)


class PurchaseItemsSerializer(PaymentServiceSerializer):
    user_uuid_from = serializers.UUIDField()
    user_uuid_to = serializers.UUIDField()
    items_payment_data = ItemPaymentData(many=True)
    return_url = serializers.URLField()
    price_with_commission = MoneySerializer()


class RefundSerializer(serializers.Serializer):
    user_uuid = serializers.UUIDField()
    item_uuid = serializers.UUIDField()

    def to_internal_value(self, data):
        if 'offer_uuid' in data.keys():
            data['item_uuid'] = data['offer_uuid']
            del data['offer_uuid']
        return super().to_internal_value(data)


class ItemHistorySerializer(serializers.Serializer):
    item_uuid = serializers.UUIDField()
    item_price = MoneySerializer()
    created_at = serializers.DateTimeField()
