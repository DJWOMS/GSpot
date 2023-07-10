from uuid import UUID

import rollbar
from apps.base.exceptions import AttemptsLimitExceededError
from apps.base.schemas import URL, PaymentServices
from apps.base.utils.db_query import multiple_select_or_404
from apps.external_payments.services.invoice_execution import execute_invoice_operations
from apps.external_payments.services.payment_serivces.yookassa_service import (
    YookassaService,
)
from apps.payment_accounts.exceptions import InsufficientFundsError
from apps.payment_accounts.models import Account, BalanceChange
from apps.payment_accounts.services.payment_commission import PaymentCalculation
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.shortcuts import get_object_or_404

from ..models import Invoice, ItemPurchase, ItemPurchaseHistory
from ..schemas import ItemPaymentData, PurchaseItemsData


class ItemPurchaseRequest:
    def __init__(self, purchase_items_data: PurchaseItemsData):
        self.purchase_items_data = purchase_items_data
        self.user_account, _ = Account.objects.get_or_create(
            user_uuid=purchase_items_data.user_uuid_from,
        )
        self._validate_income_data()

    def request_items_purchase(self) -> URL | str | None:
        invoice_creator = InvoiceCreator(self.purchase_items_data, self.user_account)
        invoice_instance = invoice_creator.invoice_instance

        if self.purchase_items_data.payment_service == PaymentServices.from_balance:
            execute_invoice_operations(
                invoice_instance=invoice_instance,
                payer_account=self.user_account,
                decrease_amount=invoice_instance.items_sum_price,
            )
            return 'Success'
        return self._request_external_items_purchase(invoice_instance)

    def _request_external_items_purchase(self, invoice_instance: Invoice):
        balance_change = BalanceChange.objects.create(
            account_id=self.user_account,
            is_accepted=False,
            operation_type=BalanceChange.OperationType.DEPOSIT,
        )
        if self.purchase_items_data.payment_service == PaymentServices.yookassa:
            payment_data = YookassaService.create_purchase_items_data(
                self.purchase_items_data,
                self.user_account,
                balance_change,
                invoice_instance,
            )
            return YookassaService().request_balance_deposit_url(
                payment_data,
            )

    def _validate_income_data(self):
        if (
            self.purchase_items_data.payment_service == PaymentServices.from_balance
            and not self._is_enough_funds()
        ):
            raise InsufficientFundsError('Not enough funds on balance')
        if not self._is_invoice_price_correct():
            raise ValidationError('Invoice price and items sum price is not valid')
        self._is_developers_exists()

        if self._is_invoice_attempts_exceeded():
            rollbar.report_message(
                f'Suspicious user behaviour {self.user_account.user_uuid}.',
                'info',
            )
            raise AttemptsLimitExceededError(
                f'Too many purchase attempts for '
                f'last {settings.MINUTES_FOR_INVOICE_ATTEMPTS} minutes.',
            )

    def _is_enough_funds(self):
        return (
            self.user_account.balance.amount
            >= self.purchase_items_data.price_with_commission.amount
        )

    def _is_invoice_price_correct(self):
        items_sum_price = self.purchase_items_data.items_total_price()
        if self.purchase_items_data.payment_service == PaymentServices.from_balance:
            compare_price = items_sum_price
        else:
            compare_price = PaymentCalculation(
                payment_type=self.purchase_items_data.payment_type,
                payment_service=self.purchase_items_data.payment_service,
                payment_amount=items_sum_price,
            ).calculate_payment_with_commission()
        return compare_price == self.purchase_items_data.price_with_commission.amount

    def _is_developers_exists(self):
        developers_list = [
            item.developer_uuid for item in self.purchase_items_data.items_payment_data
        ]
        multiple_select_or_404(developers_list, Account, 'user_uuid')

    def _is_invoice_attempts_exceeded(self):
        positive_attempts = Invoice.get_positive_attempts_for_period(self.user_account)
        negative_attempts = Invoice.get_negative_attempts_for_period(self.user_account)
        if (
            positive_attempts >= settings.INVOICE_ATTEMPTS_PER_PERIOD
            or negative_attempts >= settings.INVOICE_ATTEMPTS_PER_PERIOD
        ):
            return True
        return False


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
                self.income_data.user_uuid_to,
                item_payment_data,
            )
            list_of_item_purchase.append(item_purchase)
        money_data = (
            self.income_data.price_with_commission.amount,
            self.income_data.price_with_commission.currency.value,
        )
        invoice = Invoice.objects.create(
            price_with_commission=money_data,
        )
        invoice.item_purchases.add(*list_of_item_purchase)
        self.invoice_instance = invoice
        return invoice.pk

    @staticmethod
    def create_item_purchase_instance(
        payer_account: Account,
        receiver_account: UUID,
        item_payment_data: ItemPaymentData,
    ) -> ItemPurchase:
        developer_acc = Account.objects.get(user_uuid=item_payment_data.developer_uuid)
        account_to = get_object_or_404(Account, user_uuid=receiver_account)
        money_data = (
            item_payment_data.price.amount,
            item_payment_data.price.currency.value,
        )

        item_purchase = ItemPurchase.objects.create(
            account_from=payer_account,
            account_to=account_to,
            item_price=money_data,
            item_uuid=item_payment_data.item_uuid,
            developer_id=developer_acc,
        )
        ItemPurchaseHistory.objects.create(
            item_purchase_id=item_purchase,
            event_type=ItemPurchaseHistory.ItemPurchaseType.CREATED,
        )
        return item_purchase


class ItemPurchaseHistoryData:
    def __init__(self, user_uuid: UUID):
        self.user_uuid = user_uuid

    def get_item_purchase_qs(self):
        q_exclude_complete = Q(event_type=ItemPurchaseHistory.ItemPurchaseType.COMPLETED)
        q_exclude_paid = Q(item_purchase_id__status=ItemPurchase.ItemPurchaseStatus.PAID)

        qs = (
            ItemPurchaseHistory.objects.select_related('item_purchase_id')
            .filter(item_purchase_id__account_from__user_uuid=self.user_uuid)
            .exclude((q_exclude_complete & q_exclude_paid))
        )
        return qs
