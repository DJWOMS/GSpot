from __future__ import annotations

import uuid
from datetime import timedelta
from decimal import Decimal

from apps.base.fields import MoneyField
from apps.payment_accounts.models import Account
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Q
from django.utils import timezone


class TransferHistory(models.Model):
    account_from_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        related_name='transfer_history_account_from',
    )
    account_to_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        related_name='transfer_history_account_to',
    )

    object_id = models.PositiveIntegerField()
    account_to = GenericForeignKey('account_to_type', 'object_id')
    account_from = GenericForeignKey('account_from_type', 'object_id')
    amount = MoneyField(
        validators=[MinValueValidator(0, message='Should be a positive value')],
        editable=False,
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        db_index=True,
    )

    def __str__(self) -> str:
        return (
            f'Account to: {self.account_to}'
            f'Account type: {self.account_type}'
            f'Date time of creation: {self.created_date}'
        )


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
    price_with_commission = MoneyField(
        validators=[MinValueValidator(0, message='Should be positive value')],
    )
    is_paid = models.BooleanField(default=False)
    created_date = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        db_index=True,
    )

    @property
    def items_sum_price(self) -> Decimal:
        return Decimal(
            sum(
                self.item_purchases.all().values_list('item_price', flat=True),
            ),
        )

    @classmethod
    def get_positive_attempts_for_period(cls, user_account: Account) -> int:
        return cls._get_invoice_attempts_for_period(
            is_paid=True,
            user_account=user_account,
        )

    @classmethod
    def get_negative_attempts_for_period(cls, user_account: Account) -> int:
        return cls._get_invoice_attempts_for_period(
            is_paid=False,
            user_account=user_account,
        )

    @classmethod
    def _get_invoice_attempts_for_period(cls, is_paid: bool, user_account: Account) -> int:
        start_date = timezone.now() - timedelta(minutes=settings.MINUTES_FOR_INVOICE_ATTEMPTS)
        return cls.objects.filter(
            Q(item_purchases__account_from=user_account)
            & Q(is_paid=is_paid)
            & Q(created_date__gte=start_date),
        ).count()

    def __str__(self):
        return f'{self.invoice_id}'

    class Meta:
        ordering = ['-created_date']
