import uuid

from django.contrib.auth.models import PermissionsMixin
from django.db import models

from base.models import BaseAbstractUser, BasePermission, BaseGroup
from django.utils.translation import gettext_lazy as _

from common.models import Country, ContactType


class DeveloperPermissionMixin(PermissionsMixin):
    class Meta:
        abstract = True


class DeveloperGroup(BaseGroup):
    class Meta(BaseGroup.Meta):
        db_table = "developer_group"
        verbose_name = _("developer group")
        verbose_name_plural = _("developer groups")


class CompanyUser(BaseAbstractUser, DeveloperPermissionMixin):
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, verbose_name=_('Developer country'))
    phone = models.CharField(max_length=12, verbose_name=_('Developer phone-number'))
    avatar = models.ImageField(blank=True, verbose_name=_('Developer avatar'))
    is_banned = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    groups = models.ManyToManyField(
        'DeveloperGroup',
        verbose_name=_("developer_groups"),
        blank=True,
        help_text=_(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        related_name='developer_set',
        related_query_name='developer',
    )

    user_permissions = models.ManyToManyField(
        'DeveloperPermission',
        verbose_name=_('developer permissions'),
        blank=True,
        help_text=_('Specific permissions for this developer.'),
        related_name='developer_permission_set',
        related_query_name='developer_permission',
    )
    company = models.OneToOneField(
        'Company',
        on_delete=models.CASCADE,
        verbose_name=_('Company'),
        related_name='all_user_this_company',
        null=True
    )
    department = models.ForeignKey(
        'Department',
        on_delete=models.CASCADE,
        verbose_name=_('Department'),
        null=True
    )

    def __str__(self):
        return self.username

    class Meta:
        db_table = "company_user"
        verbose_name = _('Company user')
        verbose_name_plural = _('Company Users')


class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.OneToOneField(
        CompanyUser,
        on_delete=models.PROTECT,
        verbose_name=_('Company owner'),
        related_name='company_owner'
    )
    contact = models.ManyToManyField(
        ContactType,
        through='CompanyContact',
        verbose_name=_('Company contact'),
        blank=True,
        related_name='contact_set',
        related_query_name='contact'
    )
    title = models.CharField(max_length=50, verbose_name=_('Company title'))
    description = models.TextField(verbose_name=_('Company description'))
    email = models.EmailField(unique=True, verbose_name=_('Company email link'))
    poster = models.ImageField(blank=True, verbose_name=_('Company poster'))
    is_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Company created date'))
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Company')


class Department(models.Model):
    id = models.IntegerField(primary_key=True)
    company = models.ForeignKey(
        'Company',
        on_delete=models.CASCADE,
        verbose_name=_('Company'),
        null=True
    )
    name = models.CharField(max_length=50, verbose_name=_('Department name'))

    class Meta:
        verbose_name = _('Company department')
        verbose_name_plural = _('Company department')


class CompanyContact(models.Model):
    type = models.ForeignKey(ContactType, on_delete=models.CASCADE, verbose_name=_('type contact'), default=1)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    value = models.CharField(max_length=150, verbose_name=_('value contact'), default='')

    def __str__(self):
        return f'{self.type__name}-{self.value}'

    class Meta:
        verbose_name = _('Company contact')
        verbose_name_plural = _('Company contacts')


class DeveloperPermission(BasePermission):

    class Meta(BasePermission.Meta):
        db_table = "Developer permission"
        verbose_name = _("Developer permission")
        verbose_name_plural = _("Developer permissions")
