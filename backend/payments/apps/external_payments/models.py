from apps.base.fields import CommissionField
from apps.payment_accounts.models import BalanceChange
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class PaymentService(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f'{self.name}'


class BalanceServiceMap(models.Model):
    payment_id = models.UUIDField(primary_key=True, editable=False, db_index=True)
    service_id = models.ForeignKey(PaymentService, on_delete=models.PROTECT)
    balance_change_id = models.ForeignKey(BalanceChange, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.payment_id}'


class PaymentCommission(models.Model):
    MAX_COMMISSION = 100

    payment_service_id = models.ForeignKey(PaymentService, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=50, verbose_name='type_of_payment')
    commission = CommissionField(
        validators=(
            MinValueValidator(0, message='Should be positive value'),
            MaxValueValidator(
                MAX_COMMISSION,
                message=f'Should be not greater than {MAX_COMMISSION}',
            ),
        ),
    )

    def __str__(self):
        return f'Type of payment: {self.payment_type}' f'Commission amount: {self.commission}'
