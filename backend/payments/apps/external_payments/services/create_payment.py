from dataclasses import asdict

from yookassa import Payment

from .. import schemas
from ..schemas import PaymentCreateDataClass


def get_yookassa_payment_url(
        payment_data: PaymentCreateDataClass,
        metadata: dict,
) -> str:

    yookassa_payment_info = schemas.YookassaPaymentCreate(
        amount=schemas.AmountDataClass(
            value=payment_data.payment_amount,
        ),
        payment_method_data=schemas.PaymentMethodData(
            type=payment_data.payment_type.value,
        ),
        confirmation=schemas.ConfirmationDataClass(
            type='redirect',
            return_url=payment_data.return_url,
        ),
        metadata=metadata,
        description=f'Пополнение на {str(payment_data.payment_amount)}',
    )
    payment = Payment.create(asdict(yookassa_payment_info))

    return payment.confirmation.confirmation_url
