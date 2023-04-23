import uuid

from django.contrib.auth.models import PermissionsMixin
from django.db import models

from common.models import BaseAbstractUser, BaseContentType, BasePermission, BaseGroup
from django.utils.translation import gettext_lazy as _

from admins.models import Country


class DeveloperPermissionMixin(PermissionsMixin):
    class Meta:
        abstract = True


class CompanyContact(models.Model):
    contact = models.ForeignKey('Contact', on_delete=models.CASCADE, related_name='contacts')
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='companys')

    def __str__(self):
        return f'{self.contact__type__name} - {self.company__title}'


class Contact(models.Model):
    type = models.ForeignKey('ContactType', on_delete=models.CASCADE, verbose_name=_('type contact'))
    value = models.CharField(max_length=150, verbose_name=_('value contact'))

    def __str__(self):
        return f'{self.type__name}-{self.value}'

    class Meta:
        verbose_name = _('Company contact')
        verbose_name_plural = _('Company contacts')


class ContactType(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('name contact'))
    icon = models.ImageField(verbose_name=_('icon contact'), null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')


class DeveloperContentType(BaseContentType):
    class Meta(BaseContentType.Meta):
        db_table = "developer_content_type"
        verbose_name = _("developer content type")
        verbose_name_plural = _("developer content types")


class DeveloperPermission(BasePermission):
    content_type = models.ForeignKey(
        'DeveloperContentType',
        models.CASCADE,
        verbose_name=_("content type"),
    )

    class Meta(BasePermission.Meta):
        db_table = "developer_permission"
        verbose_name = _("developer permission")
        verbose_name_plural = _("developer permissions")


class DeveloperGroup(BaseGroup):
    permissions = models.ManyToManyField(
        DeveloperPermission, verbose_name=_("permissions"), blank=True, related_query_name="group"
    )

    class Meta(BaseGroup.Meta):
        db_table = "developer_group"
        verbose_name = _("developer group")
        verbose_name_plural = _("developer groups")


class CompanyUser(BaseAbstractUser, DeveloperPermissionMixin):
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, verbose_name=_('User country'))
    phone = models.CharField(max_length=12, verbose_name=_('User phone-number'))
    avatar = models.ImageField(blank=True, verbose_name=_('User avatar'))
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
        verbose_name=_("groups"),
        blank=True,
        help_text=_(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        related_name='user_set',
        related_query_name='user',
    )

    user_permissions = models.ManyToManyField(
        'DeveloperPermission',
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='user_set',
        related_query_name='user',
    )
    company = models.ForeignKey(
        'Company',
        on_delete=models.CASCADE,
        verbose_name=_('Company'),
        related_name='all_user_this_company',
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


class Friend(models.Model):
    user = models.ForeignKey(
        CompanyUser,
        on_delete=models.CASCADE,
        related_name='user',
        verbose_name=_('user')
    )

    friend = models.ForeignKey(
        CompanyUser,
        on_delete=models.CASCADE,
        related_name='friend',
        verbose_name=_('friend')
    )

    def __str__(self):
        return f'{self.user} - {self.friend}'