import enum
from decimal import Decimal
from typing import TypeVar

import rollbar
from apps.base.classes import ListAdminMixin
from django.contrib import admin
from django.db import transaction
from django.db.models import Model
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404
from moneyed import Money

DjangoModel = TypeVar('DjangoModel', bound=Model)


class OperationType(enum.Enum):
    WITHDRAW = 'WITHDRAW'
    DEPOSIT = 'DEPOSIT'


def add_change_balance_method(
    *,
    django_model: type[DjangoModel],
    django_field: str,
    pk: int,
    amount: Decimal,
    operation_type: OperationType,
) -> DjangoModel | HttpResponseServerError:
    if amount < 0:
        raise ValueError('Should be posotive value')
    with transaction.atomic():
        obj = get_object_or_404(
            django_model.objects.select_for_update(),
            pk=pk,
        )

        try:
            balance = getattr(obj, django_field)
            if not isinstance(balance, Money):
                raise TypeError
        except (AttributeError, TypeError) as e:
            rollbar.report_message(e, 'critical')
            return HttpResponseServerError()

        if operation_type == OperationType.DEPOSIT:
            new_balance = balance + Money(amount, balance.currency)
        elif OperationType.WITHDRAW:
            new_balance = balance - Money(amount, balance.currency)
        else:
            rollbar.report_message('Wrong operation type', 'warning')
            return HttpResponseServerError()

        setattr(obj, django_field, new_balance)
        obj.save()
    return obj


def register_admin_classes(models):
    for model in models:
        admin_class = type('AdminClass', (ListAdminMixin, admin.ModelAdmin), {})
        try:
            admin.site.register(model, admin_class)
        except admin.sites.AlreadyRegistered:
            pass
