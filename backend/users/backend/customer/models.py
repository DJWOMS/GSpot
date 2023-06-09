from datetime import date
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import Country
from base.models import BaseAbstractUser


class CustomerManager(UserManager):
    def _create_customer_user(self, username, email, phone, password, **extra_fields):
        if not username:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)
        username = CustomerUser.normalize_username(username)
        user = CustomerUser(username=username, email=email, phone=phone, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, phone=None, password=None, **extra_fields):
        return self._create_customer_user(username, email, phone, password, **extra_fields)

    def create_superuser(self, username, email=None, phone=None, password=None, **extra_fields):
        raise ValidationError(_("unable to create a superuser"))


class CustomerUser(BaseAbstractUser):
    friends = models.ManyToManyField(
        "self",
        symmetrical=True,
        through="FriendShipRequest",
        through_fields=("sender", "receiver"),
    )
    birthday = models.DateField(_("customer birthday"))
    avatar = models.ImageField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    country = models.ForeignKey(
        Country, verbose_name="Страна", on_delete=models.SET_NULL, null=True
    )

    groups = None
    user_permissions = None

    objects = CustomerManager()

    @property
    def age(self) -> int:
        today: date = date.today()
        age: int = today.year - self.birthday.year

        if today.month < self.birthday.month or (
            today.month == self.birthday.month and today.day < self.birthday.day
        ):
            age -= 1

        return age

    @property
    def permissions_codename(self) -> list[str]:
        return []

    class Meta:
        db_table = "customer"


class FriendShipRequest(models.Model):
    REQUESTED = "REQUESTED"  # запрошен
    ACCEPTED = "ACCEPTED"  # принято
    REJECTED = "REJECTED"  # отклонен

    STATUS_CHOICES = (
        (REQUESTED, "requested"),
        (ACCEPTED, "accepted"),
        (REJECTED, "rejected"),
    )
    status = models.TextField(choices=STATUS_CHOICES, default=REQUESTED)
    sender = models.ForeignKey(
        CustomerUser, on_delete=models.CASCADE, related_name="sender"
    )  # отправитель
    receiver = models.ForeignKey(
        CustomerUser, on_delete=models.CASCADE, related_name="receiver"
    )  # получатель
