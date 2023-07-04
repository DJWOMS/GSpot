import rollbar
from apps.external_payments.schemas import YookassaPayoutModel
from config.celery import app
from dacite import from_dict
from django.conf import settings
from django.db.models import F

from .exceptions import (
    InsufficientFundsError,
    NotPayoutDayError,
    NotValidAccountNumberError,
)
from .models import PayoutData
from .services.payout import PayoutProcessor


@app.task()
def make_auto_payout():
    payouts = (
        PayoutData.objects.filter(is_auto_payout=True)
        .annotate(balance=F('user_uuid__balance'))
        .iterator()
    )

    for payout in payouts:
        payout_data = {
            'amount': {
                'value': payout.balance,
                'currency': settings.DEFAULT_CURRENCY,
            },
            'payout_destination_data': {
                'type_': payout.payout_type,
                'account_number': payout.account_number,
            },
            'user_uuid': payout.user_uuid_id,
        }

        try:
            data_model_data = from_dict(
                YookassaPayoutModel,
                payout_data,
            )
        except AttributeError:
            data_model_data = YookassaPayoutModel(**payout_data)

        payout_processor = PayoutProcessor(data_model_data)

        try:
            payout_processor.create_payout()
        except (
            NotPayoutDayError,
            InsufficientFundsError,
            NotValidAccountNumberError,
        ) as error:
            rollbar.report_message(f'{error}', level='error')
