from base.choices import CurrencyChoices
from base.model_fields import AmountField, get_field_from_choices
from core.models import Product
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from ..validators import correct_date
from simple_history.models import HistoricalRecords


class PriceAbstractModel(models.Model):
    amount = AmountField('Price')
    currency = get_field_from_choices('Currency', CurrencyChoices, default=CurrencyChoices.RUB)
    created_by = models.UUIDField('Created by')
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True


class Price(PriceAbstractModel):
    updated_by = models.UUIDField('Updated by')
    updated_at = models.DateTimeField('Updated at', auto_now=True)

    class Meta:
        db_table = "price"


class SchedulerPrice(PriceAbstractModel):
    price = models.ForeignKey(Price, on_delete=models.CASCADE, related_name='scheduler_prices')
    from_dttm = models.DateTimeField('From dttm')
    to_dttm = models.DateTimeField('To dttm')
    is_active = models.BooleanField(default=False)

    class Meta:
        db_table = "scheduler_price"

    def clean(self):
        super().clean()
        correct_date(self.from_dttm, self.to_dttm)


class Offer(models.Model):
    created_by = models.UUIDField('UUID creator')
    price = models.OneToOneField(Price, on_delete=models.CASCADE, related_name='offer')
    is_active = models.BooleanField(default=False)
    products = models.ManyToManyField(Product, through='ProductOffer', related_name='offers')
    history = HistoricalRecords()

    class Meta:
        db_table = "offer"


class ProductOffer(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    created_by = models.UUIDField('UUID creator')
    created_at = models.DateTimeField('Created At', auto_now_add=True)


class Sale(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name='sales')
    from_dttm = models.DateTimeField('From dttm')
    to_dttm = models.DateTimeField('To dttm')
    discount = models.PositiveSmallIntegerField(
        'Discount', validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    is_active = models.BooleanField(default=False)
    history = HistoricalRecords()

    class Meta:
        db_table = "sale"

    def clean(self):
        super().clean()
        correct_date(self.from_dttm, self.to_dttm)
