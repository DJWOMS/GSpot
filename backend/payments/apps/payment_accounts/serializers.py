from django.conf import settings
from django.core.validators import MinValueValidator
from rest_enumfield import EnumField
from rest_framework import serializers

from apps.external_payments.schemas import PaymentTypes


class PaymentCommissionSerializer(serializers.Serializer):
    payment_amount = serializers.DecimalField(
        decimal_places=2,
        max_digits=settings.MAX_BALANCE_DIGITS,
        validators=[MinValueValidator(0, message='Insufficient Funds')],
    )
    payment_type = EnumField(choices=PaymentTypes)


class BalanceIncreaseSerializer(serializers.Serializer):
    user_uuid = serializers.UUIDField()
    payment_amount = serializers.DecimalField(
        decimal_places=2,
        max_digits=settings.MAX_BALANCE_DIGITS,
        validators=[MinValueValidator(0, message='Insufficient Funds')],
    )
    payment_type = EnumField(choices=PaymentTypes)
    return_url = serializers.URLField()
