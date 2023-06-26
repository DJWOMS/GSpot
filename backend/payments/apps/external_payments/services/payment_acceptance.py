from decimal import Decimal

from apps.base.schemas import PaymentServices, ResponseParsedData
from apps.base.utils.change_balance import accept_balance_change

from ..models import BalanceServiceMap, PaymentService
from .invoice_execution import execute_invoice_operations
from .payment_serivces.yookassa_service import YookassaService


def proceed_payment_response(income_data, payment_service: PaymentServices) -> bool:
    parsed_data = None
    if payment_service == PaymentServices.yookassa:
        parsed_data = YookassaService(income_data).handel_payment_response()
    if parsed_data is None:
        return False
    add_to_db_payout_info(parsed_data, income_data)
    if parsed_data.invoice is None:
        return True

    execute_invoice_operations(
        invoice_instance=parsed_data.invoice,
        payer_account=parsed_data.account,
        decrease_amount=parsed_data.income_amount,
    )

    return True


def add_to_db_payout_info(parsed_data: ResponseParsedData, income_data):
    payment_service, _ = PaymentService.objects.get_or_create(
        name=PaymentServices.yookassa.value,
    )
    accept_balance_change(
        balance_change_object=parsed_data.balance_object,
        amount=Decimal(parsed_data.income_amount),
    )
    BalanceServiceMap.objects.create(
        service_id=payment_service,
        payment_id=income_data.object_.id_,
        balance_change_id=parsed_data.balance_object,
        operation_type=BalanceServiceMap.OperationType.PAYOUT,
    )
