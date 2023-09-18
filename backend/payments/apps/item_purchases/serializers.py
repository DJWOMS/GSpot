from apps.base.serializer import MoneySerializer, PaymentServiceSerializer
from apps.item_purchases.models import ItemPurchase, ItemPurchaseHistory
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
    user_uuid_from = serializers.UUIDField()
    user_uuid_to = serializers.UUIDField()
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
    history_id = serializers.IntegerField(source='id')
    offer_uuid = serializers.UUIDField(source='item_purchase_id.item_uuid')
    price = MoneySerializer(source='item_purchase_id.item_price')
    purchase_type = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(source='created_date')

    STATUSES = {item.value: item.name.lower() for item in ItemPurchase.ItemPurchaseStatus}

    def get_status(self, obj: ItemPurchaseHistory):
        _status = obj.item_purchase_id.status
        if (
            _status == ItemPurchase.ItemPurchaseStatus.REFUNDED
            and obj.event_type == obj.ItemPurchaseType.CREATED
        ):
            return ItemPurchase.ItemPurchaseStatus.PAID.label.lower()
        return self.STATUSES[_status]

    def get_purchase_type(self, obj: ItemPurchaseHistory):
        if obj.item_purchase_id.account_from != obj.item_purchase_id.account_to:
            return 'gift'
        return 'for_self'
