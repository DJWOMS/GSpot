from datetime import datetime
from decimal import Decimal

from apps.base.utils import change_balance
from apps.item_purchases.models import Invoice, ItemPurchase, ItemPurchaseHistory
from apps.payment_accounts.models import Account
from django.conf import settings

from ..exceptions import ExtraTransactionHistoriesError
from ..tasks import get_item_for_self_user, gift_item_to_other_user


class InvoiceExecution:
    def __init__(self, invoice_instance: Invoice):
        self.invoice_instance = invoice_instance
        self.invoice_success_status = False

    def process_invoice_item_purchase(self):
        for invoice_item_purchase in self.invoice_instance.item_purchases.all():
            self.process_item_purchase(invoice_item_purchase)
        self.invoice_success_status = True

    def process_item_purchase(self, invoice_item_purchase: ItemPurchase) -> None:
        invoice_item_purchase.status = 'PENDING'
        invoice_item_purchase.save()

        task_execution_datetime = self.get_item_purchase_execution_date_time(
            invoice_item_purchase,
        )

        if invoice_item_purchase.account_to != invoice_item_purchase.account_from:
            get_item_for_self_user.apply_async(eta=task_execution_datetime)
        else:
            gift_item_to_other_user.apply_async(eta=task_execution_datetime)

    @staticmethod
    def get_item_purchase_execution_date_time(
        invoice_item_purchase: ItemPurchase,
    ) -> datetime:
        item_purchases_history = invoice_item_purchase.item_purchases_history.all()
        if len(item_purchases_history) > 1:
            # need to do something about this
            raise ExtraTransactionHistoriesError(
                (
                    f'For new ItemPurchase {invoice_item_purchase.pk} '
                    f'found more than 1 ItemPurchaseHistory instances'
                ),
            )

        item_purchase_history: ItemPurchaseHistory = item_purchases_history[0]
        if invoice_item_purchase.account_to == invoice_item_purchase.account_from:
            execution_date_time = settings.PERIOD_FOR_MYSELF_TASK
        else:
            execution_date_time = settings.PERIOD_FOR_GIFT_TASK
        return item_purchase_history.created_date + execution_date_time


def execute_invoice_operations(
    *,
    invoice_instance: Invoice,
    payer_account: Account,
    decrease_amount: Decimal,
):
    invoice_executioner = InvoiceExecution(invoice_instance)
    invoice_executioner.process_invoice_item_purchase()
    if invoice_executioner.invoice_success_status is True:
        # TO BE DONE: it has to put money on our shop account
        # And developer account
        change_balance.decrease_user_balance(
            account=payer_account,
            amount=decrease_amount,
        )
