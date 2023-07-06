from apps.base.fields import CommissionField
from apps.payment_accounts.models import BalanceChange
from django.db import models


class PaymentService(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f'{self.name}'


class BalanceServiceMap(models.Model):
    class OperationType(models.TextChoices):
        PAYOUT = ('PO', 'PAYOUT')
        PAYMENT = ('PM', 'PAYMENT')

    payment_id = models.CharField(editable=False, max_length=70)
    service_id = models.ForeignKey(PaymentService, on_delete=models.PROTECT)
    balance_change_id = models.ForeignKey(BalanceChange, on_delete=models.PROTECT)
    operation_type = models.CharField(max_length=20, choices=OperationType.choices)

    def __str__(self):
        return f'{self.payment_id}'


class PaymentCommission(models.Model):
    MAX_COMMISSION = 100

    payment_service_id = models.ForeignKey(PaymentService, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=50, verbose_name='type_of_payment')
    commission = CommissionField()

    def __str__(self):
        return f'Type of payment: {self.payment_type}' f'Commission amount: {self.commission}'

    class Meta:
        unique_together = ('payment_service_id', 'payment_type')

    @property
    def cache_key(self):
        return f'unique_key_{self.payment_service_id.name}_{self.payment_type}'
