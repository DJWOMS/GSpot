from django.conf import settings
from django.db.models import DecimalField
from rest_framework import serializers


class MoneyField(DecimalField):
    def __init__(
        self,
            verbose_name=None,
            name=None,
            max_digits=settings.MAX_BALANCE_DIGITS,
            decimal_places=2,
            **kwargs,
    ):
        super().__init__(
            verbose_name, name, max_digits, decimal_places, **kwargs,
        )


class MoneySerializerField(serializers.DecimalField):
    def __init__(
        self,
        min_value=0,
        max_digits=settings.MAX_BALANCE_DIGITS,
        decimal_places=2,
        **kwargs,
    ):
        super().__init__(
            max_digits, decimal_places, min_value, **kwargs,
        )
