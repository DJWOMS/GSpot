from datetime import datetime
from decimal import Decimal

import rollbar
from django.conf import settings
from django.db import transaction

from apps.payment_accounts.models import BalanceChange, Account
from apps.transactions.models import Invoice, Transaction, TransactionHistory
from .utils import parse_model_instance
from ..exceptions import BrokenInvoiceError, ExtraTransactionHistoriesError
from ..schemas import PaymentResponseStatuses, YookassaPaymentResponse
from ..tasks import get_item_for_self_user, gift_item_to_other_user


class BalanceChangeProcessor:
    def __init__(self, yookassa_response: YookassaPaymentResponse):
        self.yookassa_payment_status = yookassa_response.event
        self.payment_body = yookassa_response.object
        self.income_value = self.payment_body.income_amount.value

        self.balance_change_object = self.parse_balance_object()

    def parse_balance_object(self) -> BalanceChange | None:
        return parse_model_instance(
            django_model=BalanceChange,
            error_message=f"Can't get payment instance for payment id {self.payment_body.id}",
            pk=int(self.payment_body.metadata['balance_change_id']),
        )

    def change_user_balance(self):
        if not self.balance_change_object:
            return

        if self.yookassa_payment_status == PaymentResponseStatuses.succeeded:
            increase_user_balance(
                balance_change_object=self.balance_change_object,
                amount=Decimal(self.income_value),
            )
        elif self.yookassa_payment_status == PaymentResponseStatuses.canceled.value:
            self.balance_change_object.delete()

    @property
    def payment_status(self) -> bool:
        return self.balance_change_object is not None


def increase_user_balance(
        *,
        balance_change_object: BalanceChange,
        amount: Decimal,
) -> None:
    # in future handle situation if database not connected
    # and code below throw exception
    with transaction.atomic():
        balance_change_object.is_accepted = True
        balance_change_object.amount = amount
        balance_change_object.save()

        Account.deposit(
            pk=balance_change_object.account_id.pk,
            amount=Decimal(amount),
        )
    rollbar.report_message((
        f'Deposit {balance_change_object.amount} {settings.DEFAULT_CURRENCY} to '
        f'user account {balance_change_object.account_id}'
    ),
        'info',
    )


def decrease_user_balance(*, account_pk: int, amount: Decimal):
    with transaction.atomic():
        balance_change_object = BalanceChange.objects.create(
            account_id=account_pk,
            amount=amount,
            is_accepted=True,
            operation_type='WITHDRAW',
        )

        Account.withdraw(
            pk=account_pk,
            amount=Decimal(amount),
        )
    rollbar.report_message((
        f'Withdraw {balance_change_object.amount} {settings.DEFAULT_CURRENCY} from '
        f'user account {balance_change_object.account_id}'
    ),
        'info',
    )


class InvoiceExecution:
    def __init__(self, invoice_instance: Invoice):
        self.invoice_object = invoice_instance
        self.invoice_success_status = False

    def process_invoice(self):
        try:
            transactions_list = self.get_transactions_list()
        except BrokenInvoiceError as error:
            rollbar.report_message(
                str(error),
                'error',
            )
            self.invoice_success_status = False
            return
        for invoice_transaction in transactions_list:
            self.process_transaction(invoice_transaction)
        self.invoice_success_status = True

    def get_transactions_list(self) -> list[Transaction] | None:
        transactions_list = []
        for transaction_id in self.invoice_object.transactions:
            invoice_transaction = parse_model_instance(
                django_model=Transaction,
                error_message=f"Can't get transaction instance for transaction_id {transaction_id}",
                pk=transaction_id,
            )
            if invoice_transaction is None:
                raise BrokenInvoiceError(
                    (
                        f'Got not existing transaction  id {transaction_id}'
                        f' while parsing invoice {self.invoice_object.pk}'
                    ),
                )
            transactions_list.append(invoice_transaction)
        return transactions_list

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
