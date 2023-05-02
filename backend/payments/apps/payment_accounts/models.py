from __future__ import annotations

from apps.base.fields import CommissionField, MoneyField
from apps.base.utils.classmethod import OperationType, add_change_balance_method
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.http import HttpResponseServerError


class Account(models.Model):
    user_uuid = models.UUIDField(unique=True, editable=False, db_index=True)
    balance = MoneyField(
        validators=[MinValueValidator(0, message='Insufficient Funds')],
    )

    @classmethod
    def deposit(cls, pk, amount) -> Account | HttpResponseServerError:
        return add_change_balance_method(
            django_model=cls,
            django_field='balance',
            pk=pk,
            amount=amount,
            operation_type=OperationType.DEPOSIT,
        )

    @classmethod
    def withdraw(cls, pk, amount) -> Account | HttpResponseServerError:
        return add_change_balance_method(
            django_model=cls,
            django_field='balance',
            pk=pk,
            amount=amount,
            operation_type=OperationType.WITHDRAW,
        )

    def __str__(self) -> str:
        return f'User id: {self.user_uuid}'


class BalanceChange(models.Model):
    class OperationType(models.TextChoices):
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
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        db_index=True,
    )
    is_accepted = models.BooleanField(default=False)
    operation_type = models.CharField(max_length=20, choices=OperationType.choices)

    def __str__(self) -> str:
        return (
            f'Account id:  {self.account_id} '
            f'Date time of creation: {self.created_date}'
            f'Amount: {self.amount}'
        )

    class Meta:
        ordering = ['-created_date']


class Owner(models.Model):
    MAX_COMMISSION = 100

    revenue = MoneyField(
        validators=[MinValueValidator(0, message='Insufficient Funds')],
        editable=False,
    )
    income = MoneyField(
        validators=[MinValueValidator(0, message='Insufficient Funds')],
        editable=False,
    )
    commission = CommissionField(
        validators=(
            MinValueValidator(0, message='Should be positive value'),
            MaxValueValidator(
                MAX_COMMISSION,
                message=f'Should be not greater than {MAX_COMMISSION}',
            ),
        ),
    )
    frozen_time = models.DurationField()
    gift_time = models.DurationField()

    @classmethod
    def deposit_revenue(cls, pk, amount) -> Owner | HttpResponseServerError:
        return add_change_balance_method(
            django_model=cls,
            django_field='revenue',
            pk=pk,
            amount=amount,
            operation_type=OperationType.DEPOSIT,
        )

    @classmethod
    def withdraw_revenue(cls, pk, amount) -> Owner | HttpResponseServerError:
        return add_change_balance_method(
            django_model=cls,
            django_field='revenue',
            pk=pk,
            amount=amount,
            operation_type=OperationType.WITHDRAW,
        )

    @classmethod
    def deposit_income(cls, pk, amount) -> Owner | HttpResponseServerError:
        return add_change_balance_method(
            django_model=cls,
            django_field='income',
            pk=pk,
            amount=amount,
            operation_type=OperationType.DEPOSIT,
        )

    @classmethod
    def withdraw_income(cls, pk, amount) -> Owner | HttpResponseServerError:
        return add_change_balance_method(
            django_model=cls,
            django_field='income',
            pk=pk,
            amount=amount,
            operation_type=OperationType.WITHDRAW,
        )

    def __str__(self) -> str:
        return (
            f'Revenue: {self.revenue}'
            f'Income: {self.income}'
            f'Commission: {self.commission}'
            f'Frozen time: {self.frozen_time}'
            f'Gift time: {self.gift_time}'
        )
