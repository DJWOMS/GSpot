from apps.base.fields import MoneyAmountSerializerField
from apps.base.schemas import EnumCurrencies, PaymentServices, PaymentTypes
from rest_enumfield import EnumField
from rest_framework import serializers


class PaymentServiceSerializer(serializers.Serializer):
    payment_type = EnumField(choices=PaymentTypes)
    payment_service = EnumField(choices=PaymentServices)


class MoneySerializer(serializers.Serializer):
    amount = MoneyAmountSerializerField()
    currency = EnumField(choices=EnumCurrencies)
