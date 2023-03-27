import uuid

from django.db import models

from common.models import BaseUser, Country, BaseContentType, BasePermission, BaseGroup
from django.utils.translation import gettext_lazy as _


class CompanyUser(BaseUser):
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    phone = models.CharField(max_length=12)
    avatar = models.ImageField(blank=True)
    is_banned = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_superuser = models.BooleanField(default=False)
    friends = models.ManyToManyField('self')


class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.OneToOneField(CompanyUser, on_delete=models.PROTECT)
    title = models.CharField(max_length=50)
    description = models.TextField()
    email = models.EmailField(unique=True)
    image = models.ImageField(blank=True)
    is_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    contacts = models.ForeignKey('ContactType', on_delete=models.CASCADE)
    workers = models.ForeignKey(CompanyUser, on_delete=models.PROTECT, related_name='workers', default=0)


class ContactType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    icon = models.ImageField(blank=True)
    value = models.CharField(max_length=50)

    class Meta(BaseContentType.Meta):
        db_table = "developer_contact_type"
        verbose_name = _("developer contact type")
        verbose_name_plural = _("developer contact types")


class DeveloperContentType(BaseContentType):
    id = models.IntegerField(primary_key=True)
    service_name = models.CharField(max_length=50)
    app_label = models.CharField(max_length=50)
    model = models.CharField(max_length=50)

    class Meta(BaseContentType.Meta):
        db_table = "developer_content_type"
        verbose_name = _("developer content type")
        verbose_name_plural = _("developer content types")


class DeveloperPermission(BasePermission):
    id = models.IntegerField(primary_key=True)
    content_type = models.ForeignKey(DeveloperContentType, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    code_name = models.CharField(max_length=50)

    class Meta(BasePermission.Meta):
        db_table = "developer_permission"
        verbose_name = _("developer permission")
        verbose_name_plural = _("developer permissions")


class DeveloperUserPermissions(BasePermission):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    permission = models.ForeignKey(DeveloperPermission, on_delete=models.PROTECT)
    user = models.ForeignKey(CompanyUser, on_delete=models.PROTECT)

    class Meta(BaseGroup.Meta):
        db_table = "developer_user_permission"
        verbose_name = _("developer user permission")
        verbose_name_plural = _("developer user permissions")


class DeveloperGroup(BaseGroup):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)

    class Meta(BaseGroup.Meta):
        db_table = "developer_group"
        verbose_name = _("developer group")
        verbose_name_plural = _("developer groups")


class DeveloperGroupPermission(BaseGroup):
    id = models.IntegerField(primary_key=True)
    permission = models.ForeignKey(DeveloperPermission, on_delete=models.PROTECT, blank=True)
    group = models.ForeignKey(DeveloperGroup, on_delete=models.PROTECT)

    class Meta(BaseGroup.Meta):
        db_table = "developer_group_permission"
        verbose_name = _("developer group permission")
        verbose_name_plural = _("developer group permissions")


class DeveloperGroupUserPermissions(BaseGroup):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(DeveloperGroup, on_delete=models.PROTECT)
    user = models.ForeignKey(CompanyUser, on_delete=models.PROTECT)

    class Meta(BaseGroup.Meta):
        db_table = "developer_group_user_permission"
        verbose_name = _("developer group user permission")
        verbose_name_plural = _("developer group user permissions")
