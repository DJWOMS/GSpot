from decimal import ROUND_HALF_DOWN, Decimal

from apps.base.schemas import PaymentTypes

TWO_PLACES = Decimal(10) ** -2


def get_commission_percent(payment_type: PaymentTypes) -> Decimal:
    # maybe store that data in DB or somewhere else ?
    commission_amount = {
        payment_type.bank_card: Decimal(3.5),
        payment_type.yoo_money: Decimal(3.5),
        payment_type.sberbank: Decimal(3.5),
        payment_type.qiwi: Decimal(6),
    }
    return commission_amount[payment_type]


def calculate_payment_with_commission(
    payment_type: PaymentTypes,
    payment_amount: Decimal,
) -> Decimal:
    commission = get_commission_percent(payment_type)
    return (payment_amount * (1 / (1 - commission / 100))).quantize(
        TWO_PLACES,
        ROUND_HALF_DOWN,
    )


def calculate_payment_without_commission(
    payment_type: PaymentTypes,
    payment_amount: Decimal,
) -> Decimal:
    commission = get_commission_percent(payment_type)
    return (payment_amount * ((100 - commission) / 100)).quantize(
        TWO_PLACES,
        ROUND_HALF_DOWN,
    )
