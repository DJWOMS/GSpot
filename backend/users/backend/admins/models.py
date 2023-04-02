from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseAbstractUser, BaseContentType, BasePermission, BaseGroup


class AdminContentType(BaseContentType):
    class Meta(BaseContentType.Meta):
        db_table = "admin_content_type"
        verbose_name = _("admin content type")
        verbose_name_plural = _("admin content types")


class AdminPermission(BasePermission):
    content_type = models.ForeignKey(
        AdminContentType,
        models.CASCADE,
        verbose_name=_("content type"),
    )

    class Meta(BasePermission.Meta):
        db_table = "admin_permission"
        verbose_name = _("admin permission")
        verbose_name_plural = _("admin permissions")


class AdminGroup(BaseGroup):
    permissions = models.ManyToManyField(
        AdminPermission, verbose_name=_("permissions"), blank=True, related_query_name="group"
    )

    class Meta(BaseGroup.Meta):
        db_table = "admin_group"
        verbose_name = _("admin group")
        verbose_name_plural = _("admin groups")


class AdminPermissionMixin(PermissionsMixin):
    class Meta:
        abstract = True


class Admin(BaseAbstractUser, AdminPermissionMixin):
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
        verbose_name=_("user permissions"),
        blank=True,
        help_text=_("Specific permissions for this user."),
        related_name="user_set",
        related_query_name="user",
    )

    class Meta:
        db_table = "admin"


class Country(models.Model):
    name = models.CharField(max_length=255)
