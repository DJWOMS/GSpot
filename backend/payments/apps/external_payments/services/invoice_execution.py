from datetime import datetime

from django.conf import settings

from apps.transactions.models import Invoice, Transaction, TransactionHistory

from ..exceptions import ExtraTransactionHistoriesError


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

        # task_execution_datetime = self.get_transaction_execution_date_time(
        #     invoice_transaction,
        # )

        if invoice_transaction.account_to != invoice_transaction.account_from:
            # This part is not working has to be done
            # get_item_for_self_user.apply_async(eta=task_execution_datetime)
            pass
        else:
            # This part is not working has to be done
            # gift_item_to_other_user.apply_async(eta=task_execution_datetime)
            pass

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
