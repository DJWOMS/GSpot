from environs import Env
from yookassa import Configuration

from apps.base.schemas import URL
from apps.external_payments.schemas import PaymentCreateDataClass
from apps.external_payments.services.create_payment import \
    get_yookassa_payment_url

from ..models import Account, BalanceChange

env = Env()
env.read_env()
Configuration.account_id = env.int('SHOP_ACCOUNT_ID')
Configuration.secret_key = env.str('SHOP_SECRET_KEY')


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
