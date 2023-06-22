import datetime

from apps.base.exceptions import AttemptsLimitExceededError
from apps.base.schemas import PaymentServices
from apps.base.utils.change_balance import decrease_user_balance
from apps.external_payments.models import BalanceServiceMap, PaymentService
from apps.external_payments.schemas import YookassaPaymentStatuses, YookassaPayoutModel
from apps.external_payments.services.payment_serivces.yookassa_service import (
    YookassaPayOut,
)
from apps.payment_accounts.exceptions import (
    InsufficientFundsError,
    NotPayoutDayError,
    NotValidAccountNumberError,
)
from apps.payment_accounts.models import Account, BalanceChange, Owner
from django.conf import settings
from django.shortcuts import get_object_or_404
from yookassa.domain.exceptions import BadRequestError
from yookassa.domain.response import PayoutResponse


class PayoutProcessor:
    def __init__(self, payout_data: YookassaPayoutModel):
        self.payout_data = payout_data
        self.developer_account: Account = get_object_or_404(
            Account,
            user_uuid=self.payout_data.user_uuid,
        )
        # TODO add logic here to transform income bank card data to bank card token # noqa: T000
        # https://yookassa.ru
        # /docs/payment-solution/payouts/supplementary/collecting-data/bank-card-synonym-request

    def create_payout(self) -> str | None:
        PayOutValidator(self.payout_data, self.developer_account).validate_payout()
        response = self._request_service_payout()
        if response.status != YookassaPaymentStatuses.payout_succeeded.value:
            return 'Payment failed due to external reasons'
        self._add_to_db_payout_info(response)
        return 'Payout completed successfully'

    def _request_service_payout(self) -> PayoutResponse | None:
        data = YookassaPayOut.create_payout_data(self.payout_data, self.developer_account)
        if data is None:
            raise NotImplementedError
        try:
            response = YookassaPayOut().request_payout(data)
        except BadRequestError:
            raise NotValidAccountNumberError('Invalid account number')
        return response

    def _add_to_db_payout_info(self, payout_response: PayoutResponse):
        payment_service, _ = PaymentService.objects.get_or_create(
            name=PaymentServices.yookassa.value,
        )
        balance_change = decrease_user_balance(
            account=self.developer_account,
            amount=self.payout_data.amount.value,
        )
        BalanceServiceMap.objects.create(
            service_id=payment_service,
            payment_id=payout_response.id,
            balance_change_id=balance_change,
            operation_type=BalanceServiceMap.OperationType.PAYOUT,
        )


class PayOutValidator:
    def __init__(self, payout_model_data: YookassaPayoutModel, developer_account: Account):
        self.payout_model_data = payout_model_data
        self.developer_account = developer_account

    def validate_payout(self) -> None:
        owner = Owner.objects.first()
        if not self._is_it_payout_date(owner.payout_day_of_month):
            raise NotPayoutDayError(f'The payout day is {owner.payout_day_of_month}')

        if self._is_payout_limit_exceeded(self.developer_account):
            raise AttemptsLimitExceededError(
                (
                    f'You exceeded your payout limit '
                    f'[{settings.MAXIMUM_PAYOUTS_PER_MONTH}] for this month'
                ),
            )

        if not self._is_enough_funds():
            raise InsufficientFundsError('Developer has not required amount on balance to withdraw')

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
