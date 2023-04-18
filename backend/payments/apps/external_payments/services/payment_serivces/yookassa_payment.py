from dataclasses import asdict

import rollbar
from apps.base import utils
from apps.base.classes import AbstractPaymentClass
from apps.base.schemas import URL, ResponseParsedData
from apps.external_payments import schemas
from apps.payment_accounts.models import Account, BalanceChange
from apps.payment_accounts.schemas import BalanceIncreaseData, YookassaRequestPayment
from apps.payment_accounts.services.payment_commission import (
    calculate_payment_without_commission,
)
from apps.transactions.models import Invoice
from apps.transactions.schemas import PurchaseItemsData
from environs import Env
from yookassa import Configuration, Payment

env = Env()
env.read_env()
Configuration.account_id = env.int('SHOP_ACCOUNT_ID')
Configuration.secret_key = env.str('SHOP_SECRET_KEY')


class YookassaPayment(AbstractPaymentClass):
    def __init__(
        self,
        yookassa_response: schemas.YookassaPaymentResponse | None = None,
    ):
        self.yookassa_response = yookassa_response
        self.invoice_validator: InvoiceValidator | None = None

    def request_balance_deposit_url(
        self,
        payment_data: YookassaRequestPayment,
    ) -> URL:
        yookassa_payment_info = schemas.YookassaPaymentCreate(
            amount=schemas.AmountDataClass(
                value=payment_data.payment_amount,
            ),
            payment_method_data=schemas.PaymentMethodDataCreate(
                payment_type=payment_data.payment_type.value,
            ),
            confirmation=schemas.ConfirmationDataClass(
                confirmation_type='redirect',
                return_url=payment_data.return_url,
            ),
            metadata=payment_data.metadata,
            description=f'Пополнение на {str(payment_data.payment_amount)}',
        )

        payment = Payment.create(yookassa_payment_info.to_dict())

        return URL(payment.confirmation.confirmation_url)

    @staticmethod
    def create_balance_increase_data(
        balance_increase_data: BalanceIncreaseData,
        user_account: Account,
        balance_change: BalanceChange,
    ) -> YookassaRequestPayment:
        metadata = {
            'account_id': user_account.pk,
            'balance_change_id': balance_change.pk,
        }
        return YookassaRequestPayment(
            **asdict(balance_increase_data),
            metadata=metadata,
        )

    @staticmethod
    def create_purchase_items_data(
        purchase_items_data: PurchaseItemsData,
        user_account: Account,
        balance_change: BalanceChange,
        invoice_instance: Invoice,
    ) -> YookassaRequestPayment:
        metadata = {
            'account_id': user_account.pk,
            'balance_change_id': balance_change.pk,
            'invoice_id': str(invoice_instance.invoice_id),
        }

        return YookassaRequestPayment(
            payment_amount=invoice_instance.total_price,
            payment_service=purchase_items_data.payment_service,
            payment_type=purchase_items_data.payment_type,
            user_uuid=purchase_items_data.user_uuid,
            return_url=purchase_items_data.return_url,
            metadata=metadata,
        )

    def request_balance_withdraw_url(self, payment_data):
        pass

    def handel_payment_response(self) -> ResponseParsedData | None:
        parsed_data = self.parse_income_data()

        if parsed_data is None:
            return
        if self.yookassa_response.event == schemas.YookassaPaymentStatuses.canceled:
            parsed_data.balance_object.delete()
            return

        if parsed_data.invoice is not None:
            is_invoice_valid = self.validate_income_data(parsed_data)
            if not is_invoice_valid:
                parsed_data.invoice = None
        return parsed_data

    def parse_income_data(self) -> ResponseParsedData | None:
        return YookassaResponseParser(self.yookassa_response).parse_response()

    def validate_income_data(self, parsed_data: ResponseParsedData) -> bool:
        self.invoice_validator = InvoiceValidator(
            parsed_data.invoice,
            yookassa_response=self.yookassa_response,
        )
        return self.invoice_validator.is_invoice_valid()


class YookassaResponseParser:
    def __init__(
        self,
        yookassa_response: schemas.YookassaPaymentResponse | None = None,
    ):
        self.yookassa_response = yookassa_response
        self.payment_body = yookassa_response.object_
        self.payment_event = self.yookassa_response.event

    def parse_response(self) -> ResponseParsedData | None:
        payment_body = self.yookassa_response.object_

        payer_account = self._parse_user_account()
        if not payer_account:
            return

        balance_change_object = self._parse_balance_object()
        if not balance_change_object:
            return

        response_data = ResponseParsedData(
            account=payer_account,
            balance_object=balance_change_object,
            income_amount=self.payment_body.income_amount.value,
        )
        if (
            'invoice_id' not in self.payment_body.metadata
            or self.payment_event == schemas.YookassaPaymentStatuses.canceled
        ):
            return response_data

        invoice = self._parse_invoice_object(payment_body)
        response_data.invoice = invoice
        return response_data

    def _parse_user_account(self) -> Account:
        account_id = int(self.payment_body.metadata['account_id'])
        return utils.parse_model_instance(
            django_model=Account,
            error_message=f"Can't get user account instance for user id {account_id}",
            pk=account_id,
        )

    def _parse_balance_object(self) -> BalanceChange | None:
        return utils.parse_model_instance(
            django_model=BalanceChange,
            error_message=f"Can't get payment instance for payment id {self.payment_body.id_}",
            pk=int(self.payment_body.metadata['balance_change_id']),
        )

    @staticmethod
    def _parse_invoice_object(
        payment_body: schemas.YookassaPaymentBody,
    ) -> Invoice:
        return utils.parse_model_instance(
            django_model=Invoice,
            error_message=f"Can't get invoice instance for payment id {payment_body.id_}",
            pk=payment_body.metadata['invoice_id'],
        )


class InvoiceValidator:
    def __init__(self, invoice_object: Invoice, yookassa_response):
        self.invoice_object = invoice_object
        self.yookassa_response = yookassa_response
        self.payment_body = yookassa_response.object_
        self.income_value = self.payment_body.income_amount.value
        self.invoice_total_price = self.invoice_object.total_price
        self.error_message: str | None = None

    def is_invoice_valid(self):
        if self._is_invoice_price_correct() is False:
            return False
        if self._is_commission_correct() is False:
            return False
        return True

    def _is_invoice_price_correct(self):
        if not self.invoice_total_price == self.payment_body.amount.value:
            self.error_message = (
                f'Initial payment amount is: {self.payment_body.amount.value}'
                f'But invoice total price is: {self.invoice_total_price}'
                f'For invoice {self.invoice_object.invoice_id}'
            )
            rollbar.report_message(
                self.error_message,
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
            self.error_message = (
                f'Received payment amount: {self.income_value}'
                f'But invoice price_without_commission equal to: {price_without_commission}'
                f'For invoice {self.invoice_object.invoice_id}'
            )
            rollbar.report_message(
                self.error_message,
                'error',
            )
            return False
        return True
