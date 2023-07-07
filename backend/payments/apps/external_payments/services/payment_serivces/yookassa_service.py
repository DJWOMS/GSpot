import json
from dataclasses import asdict

import rollbar
from apps.base.classes import AbstractPaymentService, AbstractPayoutService
from apps.base.schemas import (
    URL,
    EnumCurrencies,
    ResponseParsedData,
    YookassaMoneyDataClass,
)
from apps.base.utils import change_balance
from apps.external_payments import schemas
from apps.external_payments.schemas import YookassaPayoutModel
from apps.item_purchases.models import Invoice
from apps.item_purchases.schemas import PurchaseItemsData
from apps.payment_accounts.models import Account, BalanceChange, PayoutData
from apps.payment_accounts.schemas import BalanceIncreaseData, YookassaRequestPayment
from dacite import from_dict
from django.conf import settings
from yookassa import Payment, Payout
from yookassa.domain.response import PayoutResponse


class YookassaService(AbstractPaymentService):
    def __init__(
        self,
        yookassa_response: schemas.YookassaPaymentResponse | None = None,
    ):
        settings.YOOKASSA_CONFIG.get_payment_settings()
        self.yookassa_response = yookassa_response
        self.invoice_validator: InvoiceValidator | None = None

    def request_balance_deposit_url(
        self,
        payment_data: YookassaRequestPayment,
    ) -> URL:
        yookassa_payment_info = schemas.YookassaPaymentCreate(
            amount=payment_data.amount,
            payment_method_data=schemas.PaymentMethodDataCreate(
                payment_type=payment_data.payment_type,
            ),
            confirmation=schemas.ConfirmationDataClass(
                confirmation_type='redirect',
                return_url=payment_data.return_url,
            ),
            metadata=payment_data.metadata,
            description=f'Пополнение на {str(payment_data.amount.value)}',
        )
        payment = Payment.create(json.loads(yookassa_payment_info.to_json()))

        return URL(payment.confirmation.confirmation_url)

    @staticmethod
    def create_balance_increase_data(
        balance_increase_data: BalanceIncreaseData,
        user_account: Account,
        balance_change: BalanceChange,
    ) -> YookassaRequestPayment:
        payment_data = asdict(balance_increase_data)
        payment_data['metadata'] = {
            'account_id': user_account.pk,
            'balance_change_id': balance_change.pk,
        }
        return from_dict(YookassaRequestPayment, payment_data)

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
        invoice_price = invoice_instance.price_with_commission

        return YookassaRequestPayment(
            amount=YookassaMoneyDataClass(
                value=invoice_price.amount,
                currency=EnumCurrencies[str(invoice_price.currency)],
            ),
            payment_service=purchase_items_data.payment_service,
            payment_type=purchase_items_data.payment_type,
            user_uuid=purchase_items_data.user_uuid_from,
            return_url=purchase_items_data.return_url,
            metadata=metadata,
        )

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
            else:
                parsed_data.invoice.is_paid = True
                parsed_data.invoice.save()
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

    def _parse_user_account(self) -> Account | None:
        account_id = int(self.payment_body.metadata['account_id'])
        return change_balance.parse_model_instance(
            django_model=Account,
            error_message=f"Can't get user account instance for user id {account_id}",
            pk=account_id,
        )

    def _parse_balance_object(self) -> BalanceChange | None:
        return change_balance.parse_model_instance(
            django_model=BalanceChange,
            error_message=f"Can't get payment instance for payment id {self.payment_body.id_}",
            pk=int(self.payment_body.metadata['balance_change_id']),
        )

    @staticmethod
    def _parse_invoice_object(
        payment_body: schemas.YookassaPaymentBody,
    ) -> Invoice | None:
        return change_balance.parse_model_instance(
            django_model=Invoice,
            error_message=f"Can't get invoice instance for payment id {payment_body.id_}",
            pk=payment_body.metadata['invoice_id'],
        )


class InvoiceValidator:
    def __init__(self, invoice_object: Invoice, yookassa_response):
        self.invoice_object: Invoice = invoice_object
        self.yookassa_response = yookassa_response
        self.payment_body = yookassa_response.object_
        self.income_value = self.payment_body.income_amount.value
        self.invoice_total_price = self.invoice_object.price_with_commission
        self.error_message: str | None = None

    def is_invoice_valid(self):
        return self._is_invoice_price_correct() and self._is_commission_correct()

    def _is_invoice_price_correct(self):
        if not self.invoice_total_price.amount == self.payment_body.amount.value:
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
        if self.invoice_object.items_sum_price != self.income_value:
            self.error_message = (
                f'Received payment amount: {self.income_value}'
                f'But items sum price equal to: {self.invoice_object.items_sum_price}'
                f'For invoice {self.invoice_object.invoice_id}'
            )
            rollbar.report_message(
                self.error_message,
                'error',
            )
            return False
        return True


class YookassaPayOut(AbstractPayoutService):
    def __init__(self):
        settings.YOOKASSA_CONFIG.get_payout_settings()

    def request_payout(self, payout_data: dict) -> PayoutResponse:
        return Payout.create(payout_data)

    @staticmethod
    def create_payout_data(payout_data: YookassaPayoutModel, developer_account: Account):
        response = {
            'amount': {
                'value': payout_data.amount.value,
                'currency': payout_data.amount.currency.value,
            },
            'description': f'Выплата для {developer_account.user_uuid}',
        }
        if payout_data.payout_destination_data.type_ == PayoutData.PayoutType.YOO_MONEY:
            response['payout_destination_data'] = {
                'type': payout_data.payout_destination_data.type_.value,
                'account_number': payout_data.payout_destination_data.account_number,
            }
            return response
        elif payout_data.payout_destination_data.type_ == PayoutData.PayoutType.BANK_CARD:
            # TODO add functionality to support bank card # noqa: T000
            #  https://yookassa.ru/developers/api#payout_object
            pass
        else:
            raise NotImplementedError('Not supported payout type')
