from django.db import models

from base.model_fields import get_field_from_choices, AmountField

from base.choices import CurrencyChoices, BaseTextChoices


class OrderStatusChoices(BaseTextChoices):
    WAITING_PAYMENT = "WAITING_PAYMENT", "Waiting Payment"
    COMPLETED = "COMPLETED", "Completed"
    CANCELED = "CANCELED", "Canceled"
    REFUND_REQUESTED = "REFUND_REQUESTED", "Refund Requested"
    REFUNDED = "REFUNDED", "Refunded"


class Order(models.Model):
    created_by = models.UUIDField("Created By UUID")
    currency = get_field_from_choices("Currency", CurrencyChoices, default=CurrencyChoices.RUB)
    total_amount = AmountField("Total Amount")
    total_discount = models.PositiveSmallIntegerField("Total Discount (%)")
    payment_amount = AmountField("Total Amount")
    created_at = models.DateTimeField("Created At", auto_now_add=True)
    payment_id = models.CharField("Payment Id", max_length=128, null=True)
    is_paid = models.BooleanField("Is Paid", default=False)
    gift_recipient = models.UUIDField("Recipient UUID")

    class Meta:
        db_table = "order"


class OrderStatus(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="statuses")
    status = get_field_from_choices(
        "Status", OrderStatusChoices, default=OrderStatusChoices.WAITING_PAYMENT
    )
    from_dttm = models.DateTimeField("From dttm", auto_now_add=True)

    class Meta:
        db_table = "order_status"
        ordering = ("-from_dttm",)


class OrderOfferProduct(models.Model):
    product_id = models.UUIDField("Product UUID", primary_key=True)

    class Meta:
        db_table = "order_offer_product"


class OrderOffer(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="offers")
    offer_id = models.UUIDField("Offer ID")
    price_currency = get_field_from_choices(
        "Currency", CurrencyChoices, default=CurrencyChoices.RUB
    )
    price_amount = AmountField("Price Amount")
    sale_discount = models.PositiveSmallIntegerField("Total Discount (%)")
    products = models.ManyToManyField(
        OrderOfferProduct, related_name="offers"
    )

    class Meta:
        db_table = "order_offer"
