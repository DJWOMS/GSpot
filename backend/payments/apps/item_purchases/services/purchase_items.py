from apps.base.schemas import URL, PaymentServices
from apps.external_payments.services.invoice_execution import execute_invoice_operations
from apps.external_payments.services.payment_serivces.yookassa_service import (
    YookassaService,
)
from apps.payment_accounts.models import Account, BalanceChange
from django.core.exceptions import ValidationError

from ..models import Invoice, ItemPurchase, ItemPurchaseHistory
from ..schemas import ItemPaymentData, PurchaseItemsData


def request_purchase_items(
    purchase_items_data: PurchaseItemsData,
) -> URL | str | None:
    user_account, _ = Account.objects.get_or_create(
        user_uuid=purchase_items_data.user_uuid,
    )
    if purchase_items_data.payment_service == PaymentServices.from_balance and not is_enough_funds(
        user_account,
        purchase_items_data,
    ):
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
        operation_type=BalanceChange.OperationType.DEPOSIT,
    )

    if purchase_items_data.payment_service == PaymentServices.yookassa:
        payment_data = YookassaService.create_purchase_items_data(
            purchase_items_data,
            user_account,
            balance_change,
            invoice_instance,
        )
        return YookassaService().request_balance_deposit_url(
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
        list_of_item_purchase: list[ItemPurchase] = []
        for item_payment_data in self.income_data.items_payment_data:
            item_purchase = self.create_item_purchase_instance(
                self.payer_account,
                item_payment_data,
            )
            list_of_item_purchase.append(item_purchase)

        invoice = Invoice.objects.create()
        invoice.item_purchases.add(*list_of_item_purchase)
        self.invoice_instance = invoice
        return invoice.pk

    @staticmethod
    def create_item_purchase_instance(
        payer_account: Account,
        item_payment_data: ItemPaymentData,
    ) -> ItemPurchase:
        account_to, _ = Account.objects.get_or_create(
            user_uuid=item_payment_data.owner_uuid,
        )
        item_purchase = ItemPurchase.objects.create(
            account_from=payer_account,
            account_to=account_to,
            item_price=item_payment_data.price,
            item_uuid=item_payment_data.item_uuid,
        )
        ItemPurchaseHistory.objects.create(
            item_purchase_id=item_purchase,
            operation_type='CREATED',
        )
        return item_purchase
