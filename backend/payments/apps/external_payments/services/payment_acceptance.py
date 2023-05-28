from decimal import Decimal

from apps.base.schemas import PaymentServices
from apps.base.utils import change_balance

from .invoice_execution import execute_invoice_operations
from .payment_serivces.yookassa_service import YookassaService


def proceed_payment_response(income_data, payment_service: PaymentServices) -> bool:
    parsed_data = None
    if payment_service == PaymentServices.yookassa:
        parsed_data = YookassaService(income_data).handel_payment_response()
    if parsed_data is None:
        return False

    change_balance.increase_user_balance(
        balance_change_object=parsed_data.balance_object,
        amount=Decimal(parsed_data.income_amount),
    )
    if parsed_data.invoice is None:
        return True

    execute_invoice_operations(
        invoice_instance=parsed_data.invoice,
        payer_account=parsed_data.account,
        decrease_amount=parsed_data.income_amount,
    )
    return True
