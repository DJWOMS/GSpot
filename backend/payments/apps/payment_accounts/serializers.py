from apps.external_payments.schemas import PaymentTypes
from django.conf import settings
from django.core.validators import MinValueValidator
from rest_enumfield import EnumField
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Account



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


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['user_uuid', 'balance']


class AccountOwnerSerializer(AccountSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta(AccountSerializer.Meta):
        fields = AccountSerializer.Meta.fields + ['owner']
