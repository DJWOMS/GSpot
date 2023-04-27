from django.db import models

from common.models import Country
from base.models import BaseAbstractUser


class CustomerUser(BaseAbstractUser):
    friends = models.ManyToManyField(
        'self',
        symmetrical=True,
        through='FriendShipRequest',
        through_fields=('sender', 'receiver')
    )
    avatar = models.ImageField(null=True, blank=True)
    is_banned = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    phone_number = models.CharField(
        verbose_name='Номер телефона',
        blank=True,
        max_length=15,
        null=True)
    country = models.ForeignKey(Country, verbose_name='Страна',
                                on_delete=models.SET_NULL,
                                null=True)

    class Meta:
        db_table = 'customer'


class FriendShipRequest(models.Model):
    REQUESTED = 'REQUESTED'  # запрошен
    ACCEPTED = 'ACCEPTED'    # принято
    REJECTED = 'REJECTED'    # отклонен

    STATUS_CHOICES = (
        (REQUESTED, 'requested'),
        (ACCEPTED, 'accepted'),
        (REJECTED, 'rejected')
    )
    status = models.TextField(choices=STATUS_CHOICES, default=REQUESTED)
    sender = models.ForeignKey(CustomerUser, on_delete=models.CASCADE, related_name='sender')      # отправитель
    receiver = models.ForeignKey(CustomerUser, on_delete=models.CASCADE, related_name='receiver')  # получатель
