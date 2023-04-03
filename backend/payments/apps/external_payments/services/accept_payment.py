import rollbar

from apps.external_payments.schemas import YookassaPaymentResponse
from apps.transactions.models import Invoice
from . import payment_proccessor
from .utils import parse_model_instance


def yookassa_payment_acceptance(
        yookassa_response: YookassaPaymentResponse,
) -> bool:
    payment_body = yookassa_response.object
    income_value = payment_body.income_amount.value
    account_id = int(payment_body.metadata['account_id'])
    rollbar.report_message(
        (
            f'Received payment data for: '
            f'account_id: f{account_id}'
            f'with payment amount: {income_value}'
        ),
        'info',
    )

    balance_change_processor = payment_proccessor.BalanceChangeProcessor(
        yookassa_response,
    )
    balance_change_processor.change_user_balance()
    if 'invoice_id' not in payment_body.metadata:
        return balance_change_processor.payment_status

    invoice_object = parse_model_instance(
        django_model=Invoice,
        error_message=f"Can't get invoice instance for payment id {payment_body.id}",
        pk=int(payment_body.metadata['invoice_id']),
    )
    if invoice_object.total_price != income_value:
        rollbar.report_message(
            (
                f'Received payment amount: {income_value}'
                f'But purchased price equal to: {invoice_object.total_price}'
                f'For invoice {invoice_object.invoice_id}'
            ),
            'error',
        )
        return True
    execute_invoice_operations(
        invoice_instance=invoice_object,
        account_id=account_id,
    )
    return True


def execute_invoice_operations(*, invoice_instance: Invoice, account_id: int):
    invoice_executioner = payment_proccessor.InvoiceExecution(invoice_instance)
    invoice_executioner.process_invoice()
    if invoice_executioner.invoice_success_status is True:
        payment_proccessor.decrease_user_balance(
            account_pk=account_id,
            amount=invoice_instance.total_price,
        )
