from django.core.exceptions import ValidationError

from apps.base.schemas import URL, PaymentServices
from apps.external_payments.services.invoice_execution import \
    execute_invoice_operations
from apps.external_payments.services.payment_serivces.yookassa_payment import \
    YookassaPayment
from apps.payment_accounts.models import Account, BalanceChange

from ..models import Invoice, Transaction, TransactionHistory
from ..schemas import ItemPaymentData, PurchaseItemsData


def request_purchase_items(
        purchase_items_data: PurchaseItemsData,
) -> URL | str:
    user_account, _ = Account.objects.get_or_create(
        user_uuid=purchase_items_data.user_uuid,
    )
    if purchase_items_data.payment_service == PaymentServices.from_balance \
            and not is_enough_funds(user_account, purchase_items_data):
        return 'Not enough funds on balance'

    invoice_creator = InvoiceCreator(purchase_items_data, user_account)
    invoice_instance = invoice_creator.invoice_instance

    if purchase_items_data.payment_service == PaymentServices.from_balance:
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

    if purchase_items_data.payment_service == PaymentServices.yookassa:
        payment_data = YookassaPayment.create_purchase_items_data(
            purchase_items_data,
            user_account,
            balance_change,
            invoice_instance,
        )
        return YookassaPayment().request_balance_deposit_url(
            payment_data,
        )


def is_enough_funds(user_account: Account, income_data: PurchaseItemsData):
    return user_account.balance >= income_data.total_price()


class InvoiceCreator:
    def __init__(self, income_data: PurchaseItemsData, payer_account: Account):
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
