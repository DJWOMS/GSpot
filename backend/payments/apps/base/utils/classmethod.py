import enum
from decimal import Decimal

from django.db import transaction
from django.shortcuts import get_object_or_404


class OperationType(enum.Enum):
    WITHDRAW = 'WITHDRAW'
    DEPOSIT = 'DEPOSIT'


def add_change_balance_method(
    *,
    django_model,
    django_field: str,
    pk: int,
    amount: Decimal,
    operation_type: OperationType,
):
    if amount < 0:
        raise ValueError('Should be posotive value')
    with transaction.atomic():
        obj = get_object_or_404(
            django_model.objects.select_for_update(),
            pk=pk,
        )
        balance = getattr(obj, django_field)
        if operation_type == OperationType.DEPOSIT:
            new_balance = balance + amount
        elif OperationType.WITHDRAW:
            new_balance = balance - amount
        else:
            return
        setattr(obj, django_field, new_balance)
        obj.save()
    return obj
