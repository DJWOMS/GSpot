from apps.payment_accounts.models import BalanceChange
from django.core.validators import MinValueValidator
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
    payment_service_id = models.ForeignKey(PaymentService, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=50, verbose_name='type_of_payment')
    commission = models.FloatField(
        default=0,
        validators=[MinValueValidator(0, message='indicate the amount of commission')],
    )


    def __str__(self):
        return f'Type of payment: {self.payment_type}' f'Commission amount: {self.commission}'
