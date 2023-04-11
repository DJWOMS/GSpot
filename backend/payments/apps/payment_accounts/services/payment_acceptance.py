from decimal import Decimal

import rollbar
from django.core.exceptions import ObjectDoesNotExist

from ..models import Account, BalanceChange


def payment_acceptance(response):
    try:
        table = BalanceChange.objects.get(
            id=response['object']['metadata']['table_id'],
        )
    except ObjectDoesNotExist:
        payment_id = response['object']['id']
        rollbar.report_message(
            f"Can't get table for payment id {payment_id}",
            'warning',
        )
        return False

    if response['event'] == 'payment.succeeded':
        table.is_accepted = True
        table.save()
        Account.deposit(
            pk=response['object']['metadata']['user_id'],
            amount=Decimal(response['object']['income_amount']['value']),
        )
    elif response['event'] == 'payment.canceled':
        table.delete()

    return True
