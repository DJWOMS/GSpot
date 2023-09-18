from apps.base.schemas import PaymentTypes
from rest_enumfield import EnumField
from rest_framework import serializers

from ..base.serializer import YookassaMoneySerializer
from .models import PaymentCommission, PaymentService
from .schemas import YookassaPaymentStatuses


class YookassaPaymentMethodSerializer(serializers.Serializer):
    type_ = EnumField(choices=PaymentTypes)


class YookassaPaymentBodySerializer(serializers.Serializer):
    id_ = serializers.UUIDField()
    income_amount = YookassaMoneySerializer()
    amount = YookassaMoneySerializer()
    description = serializers.CharField()
    metadata = serializers.DictField()
    payment_method = YookassaPaymentMethodSerializer()


class BaseSerializer(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        kwargs['data'] = self.rename_builtin_names(kwargs['data'])
        super().__init__(*args, **kwargs)

    def rename_builtin_names(self, old_data: dict, postfix: str = '_'):
        """
        Update json data to avoid PEP 8 name errors.
        Recursively change all built-in names of Python, adding to them
        given postfix.
        e.g. field name is `id` and postfix is `_yookassa`: id -> id_yookassa
        """

        def generate_new_key():
            builtin_names = ('id', 'type', 'object')
            if key in builtin_names:
                return key + postfix
            return key

        new_data = {}
        for key in old_data.keys():
            key_name = generate_new_key()
            if isinstance(old_data[key], dict):
                new_data[key_name] = self.rename_builtin_names(old_data[key], postfix)
            else:
                new_data[key_name] = old_data[key]

        return new_data


class YookassaPaymentAcceptanceSerializer(BaseSerializer):
    event = EnumField(choices=YookassaPaymentStatuses)
    object_ = YookassaPaymentBodySerializer()


class PaymentCommissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentCommission
        fields = '__all__'


class PaymentServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentService
        fields = '__all__'
