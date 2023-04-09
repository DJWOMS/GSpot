from django.core.exceptions import ValidationError

from apps.base.schemas import URL
from apps.external_payments.schemas import PaymentCreateDataClass, PaymentTypes
from apps.external_payments.services.accept_payment import \
    execute_invoice_operations
from apps.external_payments.services.create_payment import \
    get_yookassa_payment_url
from apps.payment_accounts.models import Account, BalanceChange

from ..models import Invoice, Transaction, TransactionHistory
from ..schemas import IncomeData, ItemPaymentData


def request_purchase_items(
        income_data: IncomeData,
) -> URL | str:
    user_account, _ = Account.objects.get_or_create(
        user_uuid=income_data.user_uuid,
    )
    if income_data.payment_type == PaymentTypes.from_balance \
            and not is_enough_funds(user_account, income_data):
        return 'Not enough funds on balance'

    invoice_creator = InvoiceCreator(income_data, user_account)
    invoice_instance = invoice_creator.invoice_instance

    if income_data.payment_type == PaymentTypes.from_balance:
        try:
            execute_invoice_operations(
                invoice_instance=invoice_instance,
                payer_account=user_account,
                decrease_amount=invoice_instance.total_price,
            )
        except ValidationError:  # maybe somehow user has not enough funds
            return 'Fail'
        return 'Success'

    balance_change = BalanceChange.objects.create(
        account_id=user_account,
        is_accepted=False,
        operation_type='DEPOSIT',
    )

    metadata = {
        'account_id': user_account.pk,
        'balance_change_id': balance_change.pk,
        'invoice_id': str(invoice_instance.invoice_id),
    }

    payment_data = PaymentCreateDataClass(
        user_uuid=income_data.user_uuid,
        payment_amount=invoice_instance.total_price,
        payment_type=income_data.payment_type,
        return_url=income_data.return_url,
    )
    return get_yookassa_payment_url(payment_data, metadata)


def is_enough_funds(user_account: Account, income_data: IncomeData):
    return user_account.balance >= income_data.total_price()


class InvoiceCreator:
    def __init__(self, income_data: IncomeData, payer_account: Account):
        self.income_data = income_data
        self.payer_account = payer_account
        self.invoice_instance: None | Invoice = None

        self.invoice_id = self.create_invoice_instance()

    def create_invoice_instance(self) -> int:
        list_of_transaction: list[Transaction] = []
        for item_payment_data in self.income_data.items_payment_data:
            transaction = self.create_transaction_instance(
                self.payer_account,
                item_payment_data,
            )
            list_of_transaction.append(transaction)

        invoice = Invoice.objects.create()
        invoice.transactions.add(*list_of_transaction)
        self.invoice_instance = invoice
        return invoice.pk

    @staticmethod
    def create_transaction_instance(
            payer_account: Account,
            item_payment_data: ItemPaymentData,
    ) -> Transaction:
        account_to, _ = Account.objects.get_or_create(
            user_uuid=item_payment_data.owner_uuid,
        )
        transaction = Transaction.objects.create(
            account_from=payer_account,
            account_to=account_to,
            item_price=item_payment_data.price,
            item_uuid=item_payment_data.item_uuid,
        )
        TransactionHistory.objects.create(
            transaction_id=transaction,
            operation_type='CREATED',
        )
        return transaction
