import datetime

from apps.external_payments.schemas import YookassaPayoutModel
from apps.external_payments.services.payment_serivces.yookassa_service import (
    YookassaPayOut,
)
from apps.payment_accounts.exceptions import (
    InsufficientFundsError,
    NotPayoutDayError,
    NotValidAccountNumberError,
    PayOutLimitExceededError,
)
from apps.payment_accounts.models import Account, BalanceChange, Owner
from django.conf import settings
from django.shortcuts import get_object_or_404
from yookassa.domain.exceptions import BadRequestError
from yookassa.domain.response import PayoutResponse


class PayoutProcessor:
    def __init__(self, payout_data: dict):
        self.payout_data = payout_data
        self.developer_account: Account = get_object_or_404(
            Account,
            user_uuid=self.payout_data.pop('user_uuid'),
        )
        # TODO add logic here to transform income bank card data to bank card token # noqa: T000
        # https://yookassa.ru
        # /docs/payment-solution/payouts/supplementary/collecting-data/bank-card-synonym-request
        self.payout_model_data = YookassaPayoutModel(**self.payout_data)

    def create_payout(self) -> PayoutResponse | None:
        PayOutValidator(self.payout_model_data, self.developer_account).validate_payout()
        return self._request_service_payout()

    def _request_service_payout(self) -> PayoutResponse | None:
        balance_change_object = BalanceChange.objects.create(
            account_id=self.developer_account,
            amount=self.payout_model_data.amount.value,
            operation_type=BalanceChange.OperationType.WITHDRAW,
        )
        data = YookassaPayOut.create_payout_data(self.payout_model_data, self.developer_account)

        try:
            response = YookassaPayOut().request_payout(data)
        except BadRequestError:
            balance_change_object.delete()
            raise NotValidAccountNumberError('Invalid account number')
        return response


class PayOutValidator:
    def __init__(self, payout_model_data: YookassaPayoutModel, developer_account: Account):
        self.payout_model_data = payout_model_data
        self.developer_account = developer_account

    def validate_payout(self) -> None:
        owner = Owner.objects.get(pk=1)
        if not self._is_it_payout_date(owner.payout_day_of_month):
            raise NotPayoutDayError(f'The payout day is {owner.payout_day_of_month}')

        if self._is_payout_limit_exceeded(self.developer_account):
            raise PayOutLimitExceededError(
                (
                    f'You exceeded your payout limit '
                    f'[{settings.MAXIMUM_PAYOUTS_PER_MONTH}] for this month'
                ),
            )

        if not self._is_enough_funds():
            raise InsufficientFundsError('Developer has not required balance to withdraw')

    @staticmethod
    def _is_it_payout_date(payout_day_of_month: int) -> bool:
        return datetime.datetime.today().day == payout_day_of_month

    def _is_payout_limit_exceeded(self, developer_account: Account) -> bool:
        return (
            BalanceChange.objects.get_payout_amount_for_last_month(developer_account)
            >= settings.MAXIMUM_PAYOUTS_PER_MONTH
        )

    def _is_enough_funds(self) -> bool:
        return self.developer_account.balance.amount > self.payout_model_data.amount.value
