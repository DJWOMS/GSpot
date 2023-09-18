import uuid

from base.utils import get_avatar_upload_path
from django.contrib.auth.models import (
    AbstractUser,
    GroupManager,
    PermissionManager,
    PermissionsMixin,
)
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseAbstractUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_("email address"), unique=True, db_index=True)
    phone = models.CharField(_("phone"), max_length=15, unique=True, default="")
    avatar = models.ImageField(null=True, blank=True, upload_to=get_avatar_upload_path)
    is_banned = models.BooleanField(default=False)
    created_at = models.DateTimeField(_("user creation date"), auto_now_add=True)
    update_at = models.DateTimeField(_("user modify date"), auto_now=True)

    is_superuser = None  # Can be overriden in child

    is_staff = None  # Remove staff field
    date_joined = None  # Remove data joined field
    last_login = None  # Remove last login field

    REQUIRED_FIELDS = ["phone", "email"]

    class Meta:
        abstract = True


class BasePermission(models.Model):
    name = models.CharField(_("name"), max_length=255)
    codename = models.CharField(_("codename"), max_length=100, unique=True)

    objects = PermissionManager()

    class Meta:
        abstract = True
        ordering = ["codename"]

    def __str__(self):
        return "%s" % self.name

    def natural_key(self):
        return self.codename


class BaseGroup(models.Model):
    name = models.CharField(_("name"), max_length=150, unique=True)
    permission = None  # Must be overridden in child class

    objects = GroupManager()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name,)


class BasePermissionMixin(PermissionsMixin):
    groups = None  # Must be overridden in child class
    user_permissions = None  # Must be overridden in child class

    def has_perm(self, perm, obj=None):
        raise NotImplementedError

    def get_all_permissions(self, obj=None):
        raise NotImplementedError

    class Meta:
        abstract = True


class BaseModerate(models.Model):
    ACTIONS = {("B", "Block"), ("U", "Unblock")}
    reason = models.CharField(
        max_length=255,
        verbose_name=_("block reason"),
        validators=[
            MinLengthValidator(3),
        ],
    )
    admin = None  # Must be overridden in child class
    date = models.DateTimeField(_("block time"), auto_now_add=True)
    action = models.CharField(max_length=1, choices=ACTIONS)

    class Meta:
        abstract = True
