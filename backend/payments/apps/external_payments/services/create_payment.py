from yookassa import Payment

from apps.base.schemas import URL

from .. import schemas


def get_yookassa_payment_url(
        payment_data: schemas.PaymentCreateDataClass,
        metadata: dict,
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
        metadata=metadata,
        description=f'Пополнение на {str(payment_data.payment_amount)}',
    )

    payment = Payment.create(yookassa_payment_info.to_dict())

    return URL(payment.confirmation.confirmation_url)
