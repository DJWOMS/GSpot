from __future__ import annotations

import uuid
from decimal import Decimal

from apps.base.fields import MoneyField
from apps.item_purchases.exceptions import DuplicateError
from apps.payment_accounts.models import Account
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class TransferHistory(models.Model):
    account_from = models.ForeignKey(
        Account,
        on_delete=models.PROTECT,
        related_name='history_accounts_from',
    )
    account_to = models.ForeignKey(
        Account,
        on_delete=models.PROTECT,
        related_name='history_accounts_to',
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
            f'Date time of creation: {self.created_date}'
        )

    class Meta:
        ordering = ['-created_date']


class ItemPurchase(models.Model):
    class ItemPurchaseStatus(models.TextChoices):
        PENDING = ('PN', 'PENDING')
        PAID = ('PD', 'PAID')
        REFUNDED = ('RF', 'REFUNDED')

    MAX_ITEM_PRICE = 10000  # in case of mistake

    account_from = models.ForeignKey(
        Account,
        on_delete=models.PROTECT,
        related_name='item_purchase_account_from',
    )
    account_to = models.ForeignKey(
        Account,
        on_delete=models.PROTECT,
        related_name='item_purchase_account_to',
    )
    developer_id = models.ForeignKey(
        Account,
        on_delete=models.PROTECT,
        related_name='developer_info',
        null=True,
    )
    item_price = MoneyField(
        validators=(
            MinValueValidator(0, message='Should be positive value'),
            MaxValueValidator(
                MAX_ITEM_PRICE,
                message=f'Should be not greater than {MAX_ITEM_PRICE}',
            ),
        ),
    )
    item_uuid = models.UUIDField(editable=False, db_index=True)
    status = models.CharField(max_length=50, choices=ItemPurchaseStatus.choices)

    def __str__(self) -> str:
        return (
            f'Account from: {self.account_from} -> '
            f'Account to: {self.account_to} '
            f'Item_uid: {self.item_uuid}'
        )


class ItemPurchaseHistory(models.Model):
    class ItemPurchaseType(models.TextChoices):
        CREATED = ('CT', 'CREATED')
        COMPLETED = ('CD', 'COMPLETED')

    item_purchase_id = models.ForeignKey(
        ItemPurchase,
        on_delete=models.PROTECT,
        related_name='item_purchases_history',
        editable=False,
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        db_index=True,
    )
    event_type = models.CharField(
        max_length=50,
        choices=ItemPurchaseType.choices,
    )

    def __str__(self) -> str:
        return (
            f'Item_purchase_id: {self.item_purchase_id}'
            f'Date time of creation: {self.created_date}'
        )

    class Meta:
        ordering = ['-created_date']


class Invoice(models.Model):
    invoice_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    item_purchases = models.ManyToManyField(ItemPurchase)
    is_paid = models.BooleanField(default=False)
    created_date = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        db_index=True,
    )

    @property
    def total_price(self) -> Decimal:
        return Decimal(
            sum(
                self.item_purchases.all().values_list('item_price', flat=True),
            ),
        )

    def __str__(self):
        return f'{self.invoice_id}'

    class Meta:
        ordering = ['-created_date']
