from apps.base.schemas import EnumCurrencies, PaymentServices, PaymentTypes
from django.conf import settings
from rest_enumfield import EnumField
from rest_framework import serializers


class PaymentServiceSerializer(serializers.Serializer):
    payment_type = EnumField(choices=PaymentTypes)
    payment_service = EnumField(choices=PaymentServices)


class MoneySerializer(serializers.Serializer):
    # amount = MoneyAmountSerializerField()
    amount = serializers.DecimalField(
        min_value=0,
        max_digits=settings.MAX_BALANCE_DIGITS,
        decimal_places=2,
    )
    currency = EnumField(choices=EnumCurrencies)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['currency'] = instance.currency.code
        return representation
