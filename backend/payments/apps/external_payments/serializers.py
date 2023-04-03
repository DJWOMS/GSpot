from django.conf import settings
from django.core.validators import MinValueValidator
from rest_enumfield import EnumField
from rest_framework import serializers

from .schemas import PaymentResponseStatuses


class AmountSerializer(serializers.Serializer):
    value = serializers.DecimalField(
        decimal_places=2,
        max_digits=settings.MAX_BALANCE_DIGITS,
        validators=[MinValueValidator(0, message='Insufficient Funds')],
    )
    currency = serializers.CharField(max_length=3)


class YookassaPaymentBodySerializer(serializers.Serializer):
    id = serializers.UUIDField()
    income_amount = AmountSerializer()
    description = serializers.CharField()
    metadata = serializers.DictField()


class YookassaPaymentAcceptanceSerializer(serializers.Serializer):
    event = EnumField(choices=PaymentResponseStatuses)
    object = YookassaPaymentBodySerializer()
