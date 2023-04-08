from __future__ import annotations

from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models, transaction
from django.shortcuts import get_object_or_404

from apps.base.fields import MoneyField


def is_amount_positive(method):
    def wrapper(cls, *args, **kwargs):
        amount = kwargs['amount']
        if amount < 0:
            raise ValueError('Should be positive value')
        return method(cls, *args, **kwargs)
    return wrapper


class Account(models.Model):
    user_uuid = models.UUIDField(unique=True, editable=False, db_index=True)
    balance = MoneyField(
        validators=[MinValueValidator(0, message='Insufficient Funds')],
        default=0,
    )

    @classmethod
    @is_amount_positive
    def deposit(cls, *, pk: int, amount: Decimal) -> Account:
        """
        Use a classmethod instead of an instance method,
        to acquire the lock we need to tell the database
        to lock it, preventing data update collisions.
        When operating on self the object is already fetched.
        And we don't have  any guaranty that it was locked.
        """
        with transaction.atomic():
            account = get_object_or_404(
                cls.objects.select_for_update(),
                pk=pk,
            )
            account.balance += amount
            account.save()
        return account

    @classmethod
    @is_amount_positive
    def withdraw(cls, *, pk: int, amount: Decimal) -> Account:
        with transaction.atomic():
            account = get_object_or_404(
                cls.objects.select_for_update(),
                pk=pk,
            )
            account.balance -= amount
            account.save()
        return account

    def __str__(self) -> str:
        return f'User id: {self.user_uuid}'


class BalanceChange(models.Model):
    class TransactionType(models.TextChoices):
        WITHDRAW = ('WD', 'WITHDRAW')
        DEPOSIT = ('DT', 'DEPOSIT')

    account_id = models.ForeignKey(
        Account,
        on_delete=models.PROTECT,
        related_name='balance_changes',
    )
    amount = MoneyField(
        validators=[MinValueValidator(0, message='Should be positive value')],
        editable=False,
        default=0,
    )
    date_time_creation = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        db_index=True,
    )
    is_accepted = models.BooleanField(default=False)
    operation_type = models.CharField(max_length=20, choices=TransactionType.choices)

    def __str__(self) -> str:
        return (
            f'Account id:  {self.account_id} '
            f'Date time of creation: {self.date_time_creation}'
            f'Amount: {self.amount}'
        )

    class Meta:
        ordering = ['-date_time_creation']
