from apps.base.schemas import URL
from apps.external_payments.schemas import PaymentCreateDataClass
from apps.external_payments.services.create_payment import get_yookassa_payment_url

from ..models import Account, BalanceChange


def request_balance_deposit_url(
    payment_data: PaymentCreateDataClass,
) -> URL:
    user_account, _ = Account.objects.get_or_create(
        user_uuid=payment_data.user_uuid,
    )

    balance_change = BalanceChange.objects.create(
        account_id=user_account,
        is_accepted=False,
        operation_type='DEPOSIT',
    )
    metadata = {
        'account_id': user_account.pk,
        'balance_change_id': balance_change.pk,
    }
    return get_yookassa_payment_url(payment_data, metadata)
