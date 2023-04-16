from datetime import datetime

from _decimal import Decimal
from django.conf import settings

from apps.base import utils
from apps.payment_accounts.models import Account
from apps.transactions.models import Invoice, Transaction, TransactionHistory

from ..exceptions import ExtraTransactionHistoriesError
from ..tasks import get_item_for_self_user, gift_item_to_other_user


class InvoiceExecution:
    def __init__(self, invoice_instance: Invoice):
        self.invoice_instance = invoice_instance
        self.invoice_success_status = False

    def process_invoice_transactions(self):
        for invoice_transaction in self.invoice_instance.transactions.all():
            self.process_transaction(invoice_transaction)
        self.invoice_success_status = True

    def process_transaction(self, invoice_transaction: Transaction) -> None:
        invoice_transaction.is_frozen = True
        invoice_transaction.save()

        task_execution_datetime = self.get_transaction_execution_date_time(
            invoice_transaction,
        )

        if invoice_transaction.account_to != invoice_transaction.account_from:
            get_item_for_self_user.apply_async(eta=task_execution_datetime)
        else:
            gift_item_to_other_user.apply_async(eta=task_execution_datetime)

    @staticmethod
    def get_transaction_execution_date_time(
            invoice_transaction: Transaction,
    ) -> datetime:
        transactions_history = invoice_transaction.transactions_history.all()
        if len(transactions_history) > 1:
            # need to do something about this
            raise ExtraTransactionHistoriesError(
                (
                    f'For new transaction {invoice_transaction.pk} '
                    f'found more than 1 TransactionHistory instances'
                ),
            )

        transaction_history: TransactionHistory = transactions_history[0]
        if invoice_transaction.account_to == invoice_transaction.account_from:
            execution_date_time = settings.PERIOD_FOR_MYSELF_TASK
        else:
            execution_date_time = settings.PERIOD_FOR_GIFT_TASK
        return transaction_history.date_time_creation + execution_date_time


def execute_invoice_operations(
        *, invoice_instance: Invoice,
        payer_account: Account,
        decrease_amount: Decimal,
):
    invoice_executioner = InvoiceExecution(invoice_instance)
    invoice_executioner.process_invoice_transactions()
    if invoice_executioner.invoice_success_status is True:
        # TO BE DONE: it has to put money on our shop account
        # And developer account
        utils.decrease_user_balance(
            account=payer_account,
            amount=decrease_amount,
        )
