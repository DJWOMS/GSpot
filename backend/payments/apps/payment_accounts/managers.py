from dateutil.relativedelta import relativedelta
from django.db import models
from django.db.models import Q
from django.utils import timezone


class BalanceChangeManager(models.Manager):
    def get_payout_amount_for_last_month(self, developer_account) -> int:
        start_date = timezone.now() - relativedelta(months=1)

        return self.filter(
            Q(account_id=developer_account)
            & Q(is_accepted=True)
            & Q(operation_type=self.model.OperationType.WITHDRAW)
            & Q(created_date__gte=start_date),
        ).count()
