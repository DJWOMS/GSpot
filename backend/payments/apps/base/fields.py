from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import DecimalField
from djmoney.models import fields
from rest_framework import serializers


class MoneyField(fields.MoneyField):
    def __init__(
        self,
        verbose_name=None,
        name=None,
        max_digits=settings.MAX_BALANCE_DIGITS,
        default_currency=settings.DEFAULT_CURRENCY,
        decimal_places=2,
        default=fields.Money('0.00', settings.DEFAULT_CURRENCY),  # noqa B008
        **kwargs,
    ):
        super().__init__(
            verbose_name=verbose_name,
            name=name,
            max_digits=max_digits,
            default_currency=default_currency,
            decimal_places=decimal_places,
            default=default,
            **kwargs,
        )


class CommissionField(DecimalField):
    def __init__(
        self,
        verbose_name=None,
        name=None,
        max_digits=5,
        decimal_places=2,
        default=0,
        **kwargs,
    ):
        kwargs['validators'] = (
            MinValueValidator(0, message='Should be positive value'),
            MaxValueValidator(
                100,
                message=f'Should be not greater than {100}',
            ),
        )

        super().__init__(
            verbose_name=verbose_name,
            name=name,
            max_digits=max_digits,
            decimal_places=decimal_places,
            default=default,
            **kwargs,
        )


class MoneyAmountSerializerField(serializers.DecimalField):
    def __init__(
        self,
        min_value=0,
        max_digits=settings.MAX_BALANCE_DIGITS,
        decimal_places=2,
        **kwargs,
    ):
        super().__init__(
            max_digits,
            decimal_places,
            min_value,
            **kwargs,
        )

    def to_representation(self, obj):
        try:
            value = super().to_representation(obj.value)
        except AttributeError:
            value = super().to_representation(obj)
        return value

    def to_internal_value(self, data):
        amount = super().to_internal_value(data)
        return amount

    def get_value(self, dictionary):
        return dictionary.get(f'{self.field_name}')


class CommissionSerializerField(serializers.DecimalField):
    def __init__(
        self,
        min_value=0,
        max_value=100,
        decimal_places=2,
        **kwargs,
    ):
        super().__init__(
            min_value,
            max_value,
            decimal_places,
            **kwargs,
        )
