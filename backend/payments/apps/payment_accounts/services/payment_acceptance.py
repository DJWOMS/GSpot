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
        rollbar.report_message(
            "Can't get table for payment id {0}".format(
                response['object']['id'],
            ),
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
