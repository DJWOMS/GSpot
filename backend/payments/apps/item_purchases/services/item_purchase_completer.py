from decimal import Decimal

from apps.base.utils.change_balance import increase_user_balance
from apps.payment_accounts.models import Owner
from config.celery import app
from django.db import transaction

from ..exceptions import RefundNotAllowedError
from ..models import Invoice, ItemPurchase, ItemPurchaseHistory, TransferHistory


class ItemPurchaseCompleter:
    def __init__(self, item_purchase: ItemPurchase, is_gift: bool = False):
        self.is_gift = is_gift
        self.item_purchase = item_purchase
        self._validate_income_data()

    def _validate_income_data(self):
        invoice = Invoice.objects.get(item_purchases=self.item_purchase)

        if (
            self.item_purchase.status != ItemPurchase.ItemPurchaseStatus.PENDING
            or invoice.is_paid is not True
        ):
            raise RefundNotAllowedError
        if (
            self.is_gift is True
            and self.item_purchase.account_from == self.item_purchase.account_to
        ):
            raise RefundNotAllowedError

    def take_refund(self):
        app.control.revoke(self.item_purchase.id, terminate=True)
        self.cancel_payment()

    def cancel_payment(self):
        owner = Owner.objects.first()

        with transaction.atomic():
            item_purchase_amount = self.item_purchase.item_price.amount
            increase_user_balance(
                account=self.item_purchase.account_from,
                amount=self.item_purchase.item_price.amount,
            )
            owner.withdraw_revenue(
                owner.pk,
                amount=item_purchase_amount,
            )
            self.item_purchase.status = ItemPurchase.ItemPurchaseStatus.REFUNDED
            self.item_purchase.save()

            ItemPurchaseHistory.objects.create(
                item_purchase_id=self.item_purchase,
                event_type=ItemPurchaseHistory.ItemPurchaseType.COMPLETED,
            )
            TransferHistory.objects.create(
                account_from=owner,
                account_to=self.item_purchase.account_from,
                amount=item_purchase_amount,
            )

    def accept_gift(self):
        app.control.revoke(self.item_purchase.id, terminate=True)
        self.accept_payment()

    def accept_payment(self):
        owner = Owner.objects.first()
        developer_income, owner_income = self._calculate_income_parts(self.item_purchase, owner)
        developer = self.item_purchase.developer_id

        with transaction.atomic():
            owner.withdraw_revenue(pk=owner.id, amount=self.item_purchase.item_price.amount)

            TransferHistory.objects.create(
                account_from=owner,
                account_to=developer,
                amount=developer_income,
            )
            TransferHistory.objects.create(
                account_from=developer,
                account_to=owner,
                amount=owner_income,
            )
            ItemPurchaseHistory.objects.create(
                item_purchase_id=self.item_purchase,
                event_type=ItemPurchaseHistory.ItemPurchaseType.COMPLETED,
            )

            increase_user_balance(
                account=developer,
                amount=developer_income,
            )
            owner.deposit_income(
                pk=owner.id,
                amount=owner_income,
            )

            self.item_purchase.status = ItemPurchase.ItemPurchaseStatus.PAID
            self.item_purchase.save()

    @staticmethod
    def _calculate_income_parts(
        item_purchase: ItemPurchase,
        owner: Owner,
    ) -> tuple[Decimal, Decimal]:
        developer_income = item_purchase.item_price.amount * ((100 - owner.commission) / 100)
        owner_income = item_purchase.item_price.amount * owner.commission / 100
        return developer_income, owner_income
