from apps.base.fields import MoneyAmountSerializerField
from apps.base.schemas import EnumCurrencies
from apps.base.serializer import PaymentServiceSerializer
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from rest_enumfield import EnumField
from rest_framework import serializers

from ..base.serializer import MoneySerializer
from .models import Account, BalanceChange, Owner, PayoutData


class PaymentCommissionSerializer(PaymentServiceSerializer):
    payment_amount = MoneyAmountSerializerField(
        validators=[MinValueValidator(0, message='Insufficient Funds')],
    )


class BalanceIncreaseSerializer(PaymentCommissionSerializer):
    user_uuid = serializers.UUIDField()
    return_url = serializers.URLField()


class AccountSerializer(serializers.ModelSerializer):
    user_uuid = serializers.UUIDField()

    class Meta:
        model = Account
        fields = ('user_uuid',)


class UUIDSerializer(serializers.Serializer):
    uuid_list = serializers.ListField(child=serializers.UUIDField())


class AmountPayoutSerializer(serializers.Serializer):
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
    currency = EnumField(choices=EnumCurrencies)


class PayoutDestination(serializers.Serializer):
    type_ = EnumField(choices=PayoutData.PayoutType)
    account_number = serializers.CharField()

    def to_internal_value(self, data):
        if 'type' in data.keys():
            data['type_'] = data['type']
            del data['type']
        return super().to_internal_value(data)


class PayoutSerializer(serializers.Serializer):
    amount = AmountPayoutSerializer()
    payout_destination_data = PayoutDestination()
    user_uuid = serializers.UUIDField()


class PayoutDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayoutData
        fields = ['account_number', 'is_auto_payout', 'payout_type']

    def validate(self, data: dict) -> dict | None:
        payout_type = data.get('payout_type')
        account_number = data.get('account_number')

        if (
            payout_type != PayoutData.PayoutType.YOO_MONEY
            or account_number is None
            or all(char.isdigit() for char in account_number)
        ):
            return data
        raise serializers.ValidationError(
            {'account_number': 'yoomoney account number should contain only digits'},
        )


class CreatePayoutDataSerializer(PayoutDataSerializer):
    user_uuid = serializers.UUIDField()

    class Meta(PayoutDataSerializer.Meta):
        fields = PayoutDataSerializer.Meta.fields + [
            'user_uuid',
        ]


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('user_uuid', 'balance', 'balance_currency')


class PayoutHistorySerializer(serializers.ModelSerializer):
    sum = MoneySerializer(source='amount')  # noqa: VNE003, A003
    created_at = serializers.DateTimeField(source='created_date')

    class Meta:
        model = BalanceChange
        fields = ('sum', 'created_at')


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'
