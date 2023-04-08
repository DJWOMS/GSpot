from decimal import Decimal

import rollbar

from apps.base import utils
from apps.external_payments.schemas import (PaymentResponseStatuses,
                                            YookassaPaymentResponse)
from apps.payment_accounts.models import Account, BalanceChange
from apps.payment_accounts.services.payment_commission import \
    calculate_payment_without_commission
from apps.transactions.models import Invoice

from . import invoice_execution as pay_proc


class YookassaIncomePayment:
    def __init__(self, yookassa_response: YookassaPaymentResponse):
        self.yookassa_response = yookassa_response
        self.payment_body = yookassa_response.object_
        self.income_value = self.payment_body.income_amount.value
        self.yookassa_payment_status = yookassa_response.event
        self.account_id = int(self.payment_body.metadata['account_id'])


class PaymentAcceptance(YookassaIncomePayment):
    def __init__(self, yookassa_response: YookassaPaymentResponse):
        super().__init__(yookassa_response)

        self.balance_handler: BalanceChangeHandler | None = None
        self.income_invoice_handler: IncomeInvoiceHandler | None = None
        self.payer_account = self.parse_user_account()

        self.payment_status = False
        self._run_payment_acceptance()

    def _run_payment_acceptance(self):
        rollbar.report_message(
            (
                f'Received payment data for: '
                f'account_id: f{self.payer_account.pk}'
                f'with payment amount: {self.income_value}'
            ),
            'info',
        )
        self.balance_handler = BalanceChangeHandler(
            self.yookassa_response,
        )
        self.balance_handler.change_user_balance()
        if 'invoice_id' not in self.payment_body.metadata:
            self.payment_status = self.balance_handler.payment_status
            return
        self.payment_status = True

        self.income_invoice_handler = IncomeInvoiceHandler(
            self.yookassa_response,
        )
        if self.income_invoice_handler.is_invoice_valid():
            execute_invoice_operations(
                invoice_instance=self.income_invoice_handler.invoice_object,
                payer_account=self.payer_account,
                decrease_amount=self.income_value,
            )

    def parse_user_account(self):
        return utils.parse_model_instance(
            django_model=Account,
            error_message=(
                f"Can't get user account instance for user id {self.account_id}"
            ),
            pk=self.account_id,
        )


class BalanceChangeHandler(YookassaIncomePayment):
    def __init__(self, yookassa_response: YookassaPaymentResponse):
        super().__init__(yookassa_response)
        self.balance_change_object = self._parse_balance_object()

    def _parse_balance_object(self) -> BalanceChange | None:
        return utils.parse_model_instance(
            django_model=BalanceChange,
            error_message=(
                f"Can't get payment instance for payment id {self.payment_body.id_}"
            ),
            pk=int(self.payment_body.metadata['balance_change_id']),
        )

    def change_user_balance(self):
        if not self.balance_change_object:
            return

        if self.yookassa_payment_status == PaymentResponseStatuses.succeeded:
            utils.increase_user_balance(
                balance_change_object=self.balance_change_object,
                amount=Decimal(self.income_value),
            )
        elif self.yookassa_payment_status == PaymentResponseStatuses.canceled.value:
            self.balance_change_object.delete()

    @property
    def payment_status(self) -> bool:
        return self.balance_change_object is not None


class IncomeInvoiceHandler(YookassaIncomePayment):
    def __init__(self, yookassa_response: YookassaPaymentResponse):
        super().__init__(yookassa_response)
        self.invoice_object = self._parse_invoice_object()
        self.invoice_total_price = self.invoice_object.total_price

    def is_invoice_valid(self):
        if self._is_invoice_price_correct() is False:
            return False
        if self._is_commission_correct() is False:
            return False
        return True

    def _parse_invoice_object(self) -> Invoice:
        return utils.parse_model_instance(
            django_model=Invoice,
            error_message=f"Can't get invoice instance for payment id {self.payment_body.id_}",
            pk=self.payment_body.metadata['invoice_id'],
        )

    def _is_invoice_price_correct(self):
        if not self.invoice_total_price == self.payment_body.amount.value:
            rollbar.report_message(
                (
                    f'Initial payment amount is: {self.payment_body.amount.value}'
                    f'But invoice total price is: {self.invoice_total_price}'
                    f'For invoice {self.invoice_object.invoice_id}'
                ),
                'error',
            )
            return False
        return True

    def _is_commission_correct(self):
        price_without_commission = calculate_payment_without_commission(
            self.payment_body.payment_method.type_,
            self.invoice_total_price,
        )
        if price_without_commission != self.income_value:
            rollbar.report_message(
                (
                    f'Received payment amount: {self.income_value}'
                    f'But invoice price_without_commission equal to: {price_without_commission}'
                    f'For invoice {self.invoice_object.invoice_id}'
                ),
                'error',
            )
            return False
        return True


def execute_invoice_operations(
        *, invoice_instance: Invoice,
        payer_account: Account,
        decrease_amount: Decimal,
):
    invoice_executioner = pay_proc.InvoiceExecution(invoice_instance)
    invoice_executioner.process_invoice_transactions()
    if invoice_executioner.invoice_success_status is True:
        # TO BE DONE: it has to put money on our shop account
        utils.decrease_user_balance(
            account=payer_account,
            amount=decrease_amount,
        )
