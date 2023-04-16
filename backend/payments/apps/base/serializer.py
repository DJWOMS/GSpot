from rest_enumfield import EnumField
from rest_framework import serializers

from apps.base.schemas import PaymentServices, PaymentTypes


class PaymentServiceSerializer(serializers.Serializer):
    payment_type = EnumField(choices=PaymentTypes)
    payment_service = EnumField(choices=PaymentServices)
