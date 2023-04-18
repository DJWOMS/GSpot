from datetime import datetime

from apps.transactions.models import Invoice, ItemPurchase, ItemPurchaseHistory
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
        invoice_item_purchase.is_frozen = True
        invoice_item_purchase.save()

        task_execution_datetime = self.get_transaction_execution_date_time(
            invoice_item_purchase,
        )

        if invoice_item_purchase.account_to != invoice_item_purchase.account_from:
            get_item_for_self_user.apply_async(eta=task_execution_datetime)
        else:
            gift_item_to_other_user.apply_async(eta=task_execution_datetime)

    @staticmethod
    def get_transaction_execution_date_time(
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
        return item_purchase_history.date_time_creation + execution_date_time
