import rollbar
from django.conf import settings
from django.db.models import F

from apps.base.classes import DRFtoDataClassMixin
from apps.external_payments.schemas import YookassaPayoutModel
from apps.payment_accounts.serializers import PayoutSerializer
from config.celery import app

from .exceptions import (
    InsufficientFundsError,
    NotPayoutDayError,
    NotValidAccountNumberError
)
from .models import PayoutData
from .services.payout import PayoutProcessor


@app.task()
def make_auto_payout():
    payouts = PayoutData.objects.filter(is_auto_payout=True).annotate(
        balance=F('user_uuid__balance')).iterator()

    for payout in payouts:
        payout_data = {
            'amount': {
                'value': payout.balance,
                'currency': settings.DEFAULT_CURRENCY
            },
            'payout_destination_data': {
                'type_': payout.payout_type,
                'account_number': payout.account_number
            },
            'user_uuid': payout.user_uuid_id
        }
        drf_to_dataclass = DRFtoDataClassMixin()
        serializer = PayoutSerializer(data=payout_data)
        serializer.is_valid(raise_exception=True)
        data_model_data = drf_to_dataclass._DRFtoDataClassMixin__convert_drf_to_dataclass(
            YookassaPayoutModel, serializer)
        payout_processor = PayoutProcessor(data_model_data)
        try:
            payout_processor.create_payout()
        except (
            NotPayoutDayError,
            InsufficientFundsError,
            NotValidAccountNumberError,
        ) as error:
            rollbar.report_message(f'{error}', level='error')
