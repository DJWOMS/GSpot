import uuid

from base.models import BaseAbstractUser, BaseGroup, BasePermission, BasePermissionMixin
from common.models import ContactType, Country
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class DeveloperPermission(BasePermission):
    class Meta(BasePermission.Meta):
        db_table = "developer_permission"
        verbose_name = _("developer permission")
        verbose_name_plural = _("developer permissions")


class DeveloperPermissionMixin(BasePermissionMixin):
    def has_perm(self, perm, obj=None):
        queryset = self.user_permissions.filter(codename=perm) | DeveloperPermission.objects.filter(
            developergroup__companyuser=self,
            codename=perm,
        )
        return queryset.exists()

    def get_all_permissions(self, obj=None):
        return self.user_permissions.all() | DeveloperPermission.objects.filter(
            developergroup__companyuser=self,
        )

    class Meta:
        abstract = True


class DeveloperGroup(BaseGroup):
    permission = models.ManyToManyField(
        DeveloperPermission,
        verbose_name=_("permission"),
        blank=True,
        related_name="developergroup_set",
        related_query_name="developergroup",
    )

    class Meta(BaseGroup.Meta):
        db_table = "developer_group"
        verbose_name = _("developer group")
        verbose_name_plural = _("developer groups")


class CompanyUserManager(UserManager):
    def _create_company_user(self, username, email, phone, password, **extra_fields):
        if not username:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)
        username = CompanyUser.normalize_username(username)
        user = CompanyUser(username=username, email=email, phone=phone, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, phone=None, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_company_user(username, email, phone, password, **extra_fields)

    def create_superuser(self, username, email=None, phone=None, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_company_user(username, email, phone, password, **extra_fields)


class CompanyUser(BaseAbstractUser, DeveloperPermissionMixin):
    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("Developer country"),
    )
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        "DeveloperGroup",
        verbose_name=_("developer_groups"),
        blank=True,
        help_text=_(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups.",
        ),
        related_name="companyuser_set",
        related_query_name="companyuser",
    )

    user_permissions = models.ManyToManyField(
        "DeveloperPermission",
        verbose_name=_("developer permissions"),
        blank=True,
        help_text=_("Specific permissions for this developer."),
        related_name="companyuser_set",
        related_query_name="companyuser",
    )
    company = models.ForeignKey(
        "Company",
        on_delete=models.CASCADE,
        verbose_name=_("Company"),
        related_name="companyuser_set",
        blank=True,
        null=True,
    )

    objects = CompanyUserManager()

    @property
    def permissions_codename(self) -> list[str]:
        return list(self.user_permissions.values_list("codename", flat=True))

    def __str__(self):
        return self.username

    class Meta:
        db_table = "company_user"
        verbose_name = _("company user")
        verbose_name_plural = _("company users")


class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.OneToOneField(
        CompanyUser,
        on_delete=models.PROTECT,
        verbose_name=_("Company owner"),
        related_name="company_owner",
    )
    contact = models.ManyToManyField(
        ContactType,
        through="CompanyContact",
        verbose_name=_("Company contact"),
        blank=True,
        related_name="contact_set",
        related_query_name="contact",
    )
    title = models.CharField(max_length=50, verbose_name=_("Company title"))
    description = models.TextField(verbose_name=_("Company description"))
    email = models.EmailField(unique=True, verbose_name=_("Company email link"))
    image = models.ImageField(blank=True, verbose_name=_("Company poster"))
    is_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Company created date"))
    is_active = models.BooleanField(default=True)
    is_banned = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "company"
        verbose_name = _("company")
        verbose_name_plural = _("companies")


class CompanyContact(models.Model):
    type = models.ForeignKey(
        ContactType,
        on_delete=models.CASCADE,
        verbose_name=_("type contact"),
    )
    company = models.ForeignKey(
        Company,
        verbose_name=_("company contacts"),
        on_delete=models.CASCADE,
    )
    value = models.CharField(max_length=150, verbose_name=_("value contact"), default="")

    def __str__(self):
        return f"{self.type.name}-{self.value}"

    class Meta:
        db_table = "company_contact"
        verbose_name = _("company contact")
        verbose_name_plural = _("company contacts")
