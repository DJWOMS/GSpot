from apps.base.serializer import MoneySerializer, PaymentServiceSerializer
from djmoney.contrib.django_rest_framework import MoneyField
from rest_framework import serializers

from apps.item_purchases.models import ItemPurchase


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


class ItemPurchaseHistorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    item_uuid = serializers.UUIDField(source='item_purchase_id.item_uuid')
    item_price = MoneyField(source='item_purchase_id.item_price', max_digits=10, decimal_places=2)
    item_price_currency = serializers.CharField(source='item_purchase_id.item_price_currency')
    status = serializers.SerializerMethodField()
    gift = serializers.SerializerMethodField()
    created_date = serializers.DateTimeField()

    def get_status(self, obj):
        _status = obj.item_purchase_id.status
        if _status == ItemPurchase.ItemPurchaseStatus.REFUNDED and obj.event_type == obj.ItemPurchaseType.CREATED:
            return ItemPurchase.ItemPurchaseStatus.PAID
        return _status

    def get_gift(self, obj):
        return obj.item_purchase_id.account_from != obj.item_purchase_id.account_to
