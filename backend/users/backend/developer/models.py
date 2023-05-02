import uuid

from django.contrib.auth.models import PermissionsMixin
from django.db import models

from base.models import BaseAbstractUser, BasePermission, BaseGroup, BasePermissionMixin
from django.utils.translation import gettext_lazy as _

from common.models import Country, ContactType


class DeveloperPermission(BasePermission):
    class Meta(BasePermission.Meta):
        db_table = "Developer_permission"
        verbose_name = _("Developer permission")
        verbose_name_plural = _("Developer permissions")


class DeveloperPermissionMixin(BasePermissionMixin):

    def has_perm(self, perm, obj=None):
        queryset = self.user_permissions.filter(codename=perm) | DeveloperPermission.objects.filter(
            developergroup__developer=self, codename=perm)
        return queryset.exists()

    def get_all_permissions(self, obj=None):
        return self.user_permissions.all() | DeveloperPermission.objects.filter(developergroup__developer=self)

    class Meta:
        abstract = True


class DeveloperGroup(BaseGroup):
    permission = models.ManyToManyField(
        DeveloperPermission,
        verbose_name=_("permission"),
        blank=True,
        related_name='developergroup_set',
        related_query_name='developergroup'
    )

    class Meta(BaseGroup.Meta):
        db_table = "developer_group"
        verbose_name = _("developer group")
        verbose_name_plural = _("developer groups")


class CompanyUser(BaseAbstractUser, DeveloperPermissionMixin):
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, verbose_name=_('Developer country'))
    avatar = models.ImageField(blank=True, verbose_name=_('Developer avatar'))
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        'DeveloperGroup',
        verbose_name=_("developer_groups"),
        blank=True,
        help_text=_(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        related_name='companyuser_set',
        related_query_name='companyuser',
    )

    user_permissions = models.ManyToManyField(
        'DeveloperPermission',
        verbose_name=_('developer permissions'),
        blank=True,
        help_text=_('Specific permissions for this developer.'),
        related_name='companyuser_set',
        related_query_name='companyuser',
    )
    company = models.ForeignKey(
        'Company',
        on_delete=models.CASCADE,
        verbose_name=_('Company'),
        related_name='companyuser_set',
        blank=True,
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
    image = models.ImageField(blank=True, verbose_name=_('Company poster'))
    is_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Company created date'))
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Company')


class CompanyContact(models.Model):
    type = models.ForeignKey(
        ContactType,
        on_delete=models.CASCADE,
        verbose_name=_("type contact"),
    )
    company = models.ForeignKey(
        Company,
        verbose_name=_("company contacts"),
        on_delete=models.CASCADE
    )
    value = models.CharField(max_length=150, verbose_name=_('value contact'), default='')

    def __str__(self):
        return f'{self.type__name}-{self.value}'

    class Meta:
        verbose_name = _('Company contact')
        verbose_name_plural = _('Company contacts')
