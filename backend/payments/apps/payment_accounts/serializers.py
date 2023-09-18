from apps.base.fields import MoneyAmountSerializerField
from apps.base.serializer import (
    AmountPayoutSerializer,
    PaymentServiceSerializer,
    YookassaMoneySerializer,
)
from django.core.validators import MinValueValidator
from rest_enumfield import EnumField
from rest_framework import serializers

from ..base.serializer import MoneySerializer
from .models import Account, BalanceChange, Owner, PayoutData


class CalculateCommissionSerializer(PaymentServiceSerializer):
    payment_amount = MoneyAmountSerializerField(
        validators=[MinValueValidator(0, message='Insufficient Funds')],
    )


class BalanceIncreaseSerializer(PaymentServiceSerializer):
    user_uuid = serializers.UUIDField()
    return_url = serializers.URLField()
    amount = YookassaMoneySerializer()


class AccountSerializer(serializers.ModelSerializer):
    user_uuid = serializers.UUIDField()

    class Meta:
        model = Account
        fields = ('user_uuid',)


class UUIDSerializer(serializers.Serializer):
    uuid_list = serializers.ListField(child=serializers.UUIDField())


class PayoutDestination(serializers.Serializer):
    type_ = EnumField(choices=PayoutData.PayoutType)
    account_number = serializers.CharField()

    def to_internal_value(self, data):
        if 'type' in data.keys():
            data['type_'] = data['type']
            del data['type']
        return super().to_internal_value(data)


class WithdrawSerializer(serializers.Serializer):
    amount = AmountPayoutSerializer()
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


class BalanceHistorySerializer(serializers.ModelSerializer):
    sum = MoneySerializer(source='amount')  # noqa: VNE003, A003
    created_at = serializers.DateTimeField(source='created_date')

    class Meta:
        model = BalanceChange
        fields = ('sum', 'created_at')


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'
