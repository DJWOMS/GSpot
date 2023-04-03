from __future__ import annotations

import uuid

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from marshmallow.fields import Decimal

from apps.payment_accounts.models import Account
from apps.transactions.exceptions import DuplicateError


class TransferHistory(models.Model):
    account_from = models.ForeignKey(
        Account, on_delete=models.PROTECT, related_name='history_accounts_from',
    )
    account_to = models.ForeignKey(
        Account, on_delete=models.PROTECT, related_name='history_accounts_to',
    )
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=settings.MAX_BALANCE_DIGITS,
        validators=[MinValueValidator(0, message='Should be positive value')],
        editable=False,
    )
    date_time_creation = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        db_index=True,
    )

    def clean(self):
        if self.account_from == self.account_to:
            raise DuplicateError(
                'account_from and account_to should be different values',
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return (
            f'Account from: {self.account_from} -> '
            f'Account to: {self.account_to}'
            f'Date time of creation: {self.date_time_creation}'
        )

    class Meta:
        ordering = ['-date_time_creation']


class Transaction(models.Model):
    MAX_ITEM_PRICE = 10000  # in case of mistake

    account_from = models.ForeignKey(
        Account, on_delete=models.PROTECT,
        related_name='transactions_account_from',
    )
    account_to = models.ForeignKey(
        Account, on_delete=models.PROTECT,
        related_name='transactions_account_to',
    )
    item_price = models.DecimalField(
        decimal_places=2,
        max_digits=settings.MAX_BALANCE_DIGITS,
        validators=[
            MinValueValidator(0, message='Should be positive value'),
            MaxValueValidator(
                MAX_ITEM_PRICE,
                message=f'Should be not greater than {MAX_ITEM_PRICE}',
            ),
        ],
    )
    item_uuid = models.UUIDField(editable=False, db_index=True)
    is_frozen = models.BooleanField(default=False)
    is_accepted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return (
            f'Account from: {self.account_from} -> '
            f'Account to: {self.account_to} '
            f'Item_uid: {self.item_uuid}'
        )


class TransactionHistory(models.Model):
    class TransactionType(models.TextChoices):
        CREATED = ('CT', 'CREATED')
        COMPLETED = ('CD', 'COMPLETED')

    transaction_id = models.ForeignKey(
        Transaction,
        on_delete=models.PROTECT,
        related_name='transactions_history',
        editable=False,
    )
    date_time_creation = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        db_index=True,
    )
    operation_type = models.CharField(
        max_length=50,
        choices=TransactionType.choices,
    )

    def __str__(self) -> str:
        return (
            f'Transaction_id: {self.transaction_id}'
            f'Date time of creation: {self.date_time_creation}'
        )

    class Meta:
        ordering = ['-date_time_creation']


class Invoice(models.Model):
    invoice_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    transactions = models.ManyToManyField(Transaction)

    @property
    def total_price(self) -> Decimal:
        return sum(
            self.transactions.all().values_list('item_price', flat=True),
        )

    def __str__(self):
        return f'{self.invoice_id}'
