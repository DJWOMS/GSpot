from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import BaseAbstractUser, BasePermission, BaseGroup


class AdminPermission(BasePermission):

    class Meta(BasePermission.Meta):
        db_table = "permission"
        verbose_name = _("permission")
        verbose_name_plural = _("permissions")


class AdminPermissionMixin(PermissionsMixin):
    class Meta:
        abstract = True


class AdminGroup(BaseGroup):
    permission = models.ManyToManyField(
        AdminPermission,
        verbose_name=_("permission"),
        blank=True,
    )

    class Meta(BaseGroup.Meta):
        db_table = "admin_group"
        verbose_name = _("admin group")
        verbose_name_plural = _("admin groups")


class Admin(BaseAbstractUser, AdminPermissionMixin):
    phone = models.CharField(max_length=15, unique=True, default='')
    avatar = models.ImageField(null=True, blank=True)
    is_banned = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    groups = models.ManyToManyField(
        AdminGroup,
        verbose_name=_("groups"),
        blank=True,
        help_text=_(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        related_name="user_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        AdminPermission,
        verbose_name=_("admin permissions"),
        blank=True,
        help_text=_("Specific permissions for this admin."),
        related_name="admin_set",
        related_query_name="admin",
    )

    class Meta:
        db_table = "admin"
