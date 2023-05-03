from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import Country
from base.models import BaseAbstractUser


class CustomerUser(BaseAbstractUser):
    friends = models.ManyToManyField(
        'self',
        symmetrical=True,
        through='FriendShipRequest',
        through_fields=('sender', 'receiver')
    )
    birthday = models.DateField(_("customer birthday"))
    avatar = models.ImageField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    country = models.ForeignKey(
        Country,
        verbose_name='Страна',
        on_delete=models.SET_NULL,
        null=True
    )

    groups = None
    user_permissions = None

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
