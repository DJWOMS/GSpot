from apps.base.fields import MoneyAmountSerializerField
from apps.base.schemas import EnumCurrencies, PaymentServices, PaymentTypes
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from rest_enumfield import EnumField
from rest_framework import serializers


class PaymentServiceSerializer(serializers.Serializer):
    payment_type = EnumField(choices=PaymentTypes)
    payment_service = EnumField(choices=PaymentServices)


class CurrencySerializer(serializers.Serializer):
    currency = EnumField(choices=EnumCurrencies)


class MoneySerializer(CurrencySerializer):
    amount = MoneyAmountSerializerField(
        validators=[MinValueValidator(0, message='Insufficient Funds')],
    )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['currency'] = instance.currency.code
        return representation


class YookassaMoneySerializer(CurrencySerializer):
    value = MoneyAmountSerializerField(
        validators=[MinValueValidator(0, message='Insufficient Funds')],
    )


class AmountPayoutSerializer(CurrencySerializer):
    value = MoneyAmountSerializerField(
        validators=[
            MinValueValidator(
                settings.MINIMUM_PAYOUT_AMOUNT,
                message=f'Should be more then {settings.MINIMUM_PAYOUT_AMOUNT}',
            ),
            MaxValueValidator(
                settings.MAXIMUM_YOOKASSA_PAYOUT,
                message=f'Payout service limit exceeded {settings.MAXIMUM_YOOKASSA_PAYOUT}',
            ),
        ],
    )
