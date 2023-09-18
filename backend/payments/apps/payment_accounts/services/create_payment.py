from environs import Env
from yookassa import Configuration, Payment

from ..models import Account, BalanceChange

env = Env()
env.read_env()
Configuration.account_id = env.int('account_id')
Configuration.secret_key = env.str('shop_secret_key')


def create_payment(serialized_data):
    uuid = serialized_data.get('uuid')
    value = serialized_data.get('value')
    commission = serialized_data.get('commission')
    payment_type = serialized_data.get('payment_type')
    return_url = serialized_data.get('return_url')
    value_with_commission = value * (1 / (1 - commission / 100))
    user_account, created = Account.objects.get_or_create(user_uid=uuid)

    change = BalanceChange.objects.create(
        account_id=user_account,
        amount=value,
        is_accepted=False,
        operation_type='DEPOSIT',
    )

    payment = Payment.create({
        'amount': {
            'value': value_with_commission,
            'currency': 'RUB',
        },
        'payment_method_data': {
            'type': payment_type,
        },
        'confirmation': {
            'type': 'redirect',
            'return_url': return_url,
        },
        'metadata': {
            'table_id': change.id,
            'user_id': user_account.id,
        },
        'capture': True,
        'refundable': False,
        'description': 'Пополнение на ' + str(value),
    })

    return payment.confirmation.confirmation_url
