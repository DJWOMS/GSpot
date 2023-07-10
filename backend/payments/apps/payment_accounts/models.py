from __future__ import annotations

from apps.base.fields import CommissionField, MoneyField
from apps.base.utils.classmethod import OperationType, add_change_balance_method
from apps.payment_accounts.managers import BalanceChangeManager
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.http import HttpResponseServerError
from yookassa.domain.common import PaymentMethodType


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
        return f'User uuid: {self.user_uuid}'


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

    objects = BalanceChangeManager()

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
    commission = CommissionField()
    frozen_time = models.DurationField()
    gift_time = models.DurationField()
    payout_day_of_month = models.IntegerField(
        validators=(
            MinValueValidator(1, message='The value must be at least 1'),
            MaxValueValidator(28, message='The value should be no more than 28'),
        ),
    )

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

    def save(self, *args, **kwargs):
        if not self.pk and Owner.objects.exists():
            raise ValidationError('There is can be only one Owner instance')
        return super(Owner, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return (
            f'Revenue: {self.revenue}'
            f'Income: {self.income}'
            f'Commission: {self.commission}'
            f'Frozen time: {self.frozen_time}'
            f'Gift time: {self.gift_time}'
        )


class PayoutData(models.Model):
    class PayoutType(models.TextChoices):
        BANK_CARD = (PaymentMethodType.BANK_CARD, 'BANK_CARD')
        YOO_MONEY = (PaymentMethodType.YOO_MONEY, 'YOO_MONEY')

    user_uuid = models.OneToOneField(
        Account,
        to_field='user_uuid',
        primary_key=True,
        on_delete=models.CASCADE,
        related_name='payout_data',
        editable=False,
    )
    account_number = models.CharField(max_length=30)
    is_auto_payout = models.BooleanField(default=False)
    payout_type = models.CharField(max_length=23, choices=PayoutType.choices)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['account_number', 'payout_type'],
                name='unique payout data',
            ),
        ]

    def __str__(self):
        return (
            f'Account id: {self.user_uuid.pk} '
            f'Account number: {self.account_number} '
            f'Payout_type: {self.payout_type}'
        )
