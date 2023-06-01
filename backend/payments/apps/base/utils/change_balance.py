from decimal import Decimal
from typing import TypeVar

import rollbar
from apps.payment_accounts.models import Account, BalanceChange
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.db.models import Model

DjangoModel = TypeVar('DjangoModel', bound=Model)


def parse_model_instance(
    *,
    django_model: type[DjangoModel],
    error_message: str,
    pk: int,
) -> DjangoModel | None:
    try:
        django_model_instance = django_model.objects.get(pk=pk)
    except ObjectDoesNotExist:
        rollbar.report_message(error_message, 'warning')
        return None

    return django_model_instance


def edit_change_balance(
    *,
    balance_change_object: BalanceChange,
    amount: Decimal,
) -> None:
    with transaction.atomic():
        balance_change_object.is_accepted = True
        balance_change_object.amount = amount
        balance_change_object.save()

        Account.deposit(
            pk=balance_change_object.account_id.pk,
            amount=Decimal(amount),
        )
    rollbar.report_message(
        (
            f'Deposit {balance_change_object.amount} {settings.DEFAULT_CURRENCY} '
            f'to user account {balance_change_object.account_id}'
        ),
        'info',
    )


def increase_user_balance(*, account: Account, amount: Decimal) -> BalanceChange:
    with transaction.atomic():
        balance_change_object = BalanceChange.objects.create(
            account_id=account,
            amount=amount,
            is_accepted=True,
            operation_type=BalanceChange.OperationType.DEPOSIT,
        )

        Account.deposit(
            pk=account.pk,
            amount=Decimal(amount),
        )
    rollbar.report_message(
        (
            f'Deposit {balance_change_object.amount} {settings.DEFAULT_CURRENCY} '
            f'from user account {balance_change_object.account_id}'
        ),
        'info',
    )
    return balance_change_object


def decrease_user_balance(*, account: Account, amount: Decimal) -> BalanceChange:
    with transaction.atomic():
        balance_change_object = BalanceChange.objects.create(
            account_id=account,
            amount=amount,
            is_accepted=True,
            operation_type=BalanceChange.OperationType.WITHDRAW,
        )

        Account.withdraw(
            pk=account.pk,
            amount=Decimal(amount),
        )
    rollbar.report_message(
        (
            f'Withdraw {balance_change_object.amount} {settings.DEFAULT_CURRENCY} '
            f'from user account {balance_change_object.account_id}'
        ),
        'info',
    )
    return balance_change_object
