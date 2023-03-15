from environs import Env
from yookassa import Configuration, Payment

from ..models import Account, BalanceChange

env = Env()
env.read_env()
Configuration.account_id = env.int('account_id')
Configuration.secret_key = env.str('shop_secret_key')


def create_payment(uuid, value, commission, payment_type, return_url):
    pay_value = value * (1 / (1 - commission / 100))
    try:
        user = Account.objects.get(user_uid=uuid)
    except BaseException:
        user = Account.objects.create(
            user_uid=uuid,
        )
        user.save()

    changing = BalanceChange.objects.create(
        account_id=user,
        amount=value,
        is_accepted=False,
        operation_type='DEPOSIT',
    )
    changing.save()

    payment = Payment.create({
        'amount': {
            'value': pay_value,
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
            'table_id': changing.id,
            'user_id': user.id,
        },
        'capture': True,
        'refundable': False,
        'description': 'Пополнение на ' + str(value),
    })

    return payment.confirmation.confirmation_url
