from decimal import Decimal

from apps.external_payments.schemas import YookassaPaymentTypes, YookassaPaymentInfo


def get_commission_percent(payment_type: YookassaPaymentTypes) -> Decimal:
    # maybe store that data in DB or somewhere else ?
    commission_amount = {
        payment_type.bank_card: Decimal(3.5),
        payment_type.yoo_money: Decimal(3.5),
        payment_type.sberbank: Decimal(3.5),
        payment_type.qiwi: Decimal(6),
    }
    return commission_amount[payment_type]


def calculate_payment_with_commission(payment_info: YookassaPaymentInfo) -> Decimal:
    two_places = Decimal(10) ** -2
    commission = get_commission_percent(payment_info.payment_type)
    return (payment_info.payment_amount * (1 / (1 - commission / 100))).quantize(two_places)
