from collections import namedtuple
from unittest import mock
from unittest.mock import MagicMock, patch

from administrator.models import Admin, AdminGroup
from base.base_tests.tests import BaseViewTestCase
from base.models import BaseAbstractUser
from base.permissions import BaseUserPermissions
from base.validators import BaseUserValidation
from common.permissions.permissons import (
    CompanyEmployeePerm,
    CompanyOwnerPerm,
    IsAdminScopeUserPerm,
    IsAdminSuperUserPerm,
    IsCompanyScopeUserPerm,
    IsCompanySuperUserPerm,
    IsCustomerScopeUserPerm,
    UserPermissionCheck,
)
from common.permissions.validators import ActiveUserValidator, BannedUserValidatorVerify
from customer.models import CustomerUser
from developer.models import Company, CompanyUser, DeveloperGroup, DeveloperPermission
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request


class TestBasePermissions(BaseViewTestCase):
    @patch.object(BaseUserPermissions, "verify")
    def test_010_base_permission(self, mock_verify: MagicMock):
        mock_verify.return_value = True
        view = MagicMock()
        request = MagicMock()
        self.assertTrue(BaseUserPermissions().has_permission(request, view))
        mock_verify.return_value = False
        self.assertFalse(BaseUserPermissions().has_permission(request, view))

    @patch.object(BaseUserValidation, "verify")
    def test_020_base_validators(self, mock_verify: MagicMock):
        mock_verify.return_value = True
        user = MagicMock()
        BaseUserValidation().validate(user)
        mock_verify.return_value = False
        with self.assertRaises(ValidationError) as context:
            BaseUserValidation().validate(user)
        self.assertEqual(context.exception.detail[0], "ValidationError")
        with self.assertRaises(ValidationError) as context:
            BaseUserValidation("custom error").validate(user)
        self.assertEqual(context.exception.detail[0], "custom error")


class TestValidators(BaseViewTestCase):
    def test_010_active_user_validator(self):
        user = mock.create_autospec(BaseAbstractUser)
        user.is_active = True
        ActiveUserValidator().validate(user)
        user.is_active = False
        with self.assertRaises(ValidationError):
            ActiveUserValidator().validate(user)
        with self.assertRaises(ValidationError) as cxt:
            ActiveUserValidator("custom message").validate(user)
        self.assertEqual(cxt.exception.detail[0], "custom message")

    def test_020_banned_user_validator(self):
        user = mock.create_autospec(BaseAbstractUser)
        user.is_banned = True
        with self.assertRaises(ValidationError):
            BannedUserValidatorVerify().validate(user)
        user.is_banned = False
        BannedUserValidatorVerify().validate(user)


class TestPermissions(BaseViewTestCase):
    def setUp(self) -> None:
        self.view = MagicMock()
        self.request = mock.create_autospec(Request)

    @classmethod
    def create_user(cls, model: type[BaseAbstractUser], **kwargs) -> type[BaseAbstractUser]:
        data = {
            "username": cls.faker.word(),
            "email": cls.faker.email(),
            "phone": cls.faker.random_number(digits=10, fix_len=True),
            "password": cls.faker.word(),
            "is_active": True,
        }
        if model == CustomerUser:
            data["birthday"] = cls.faker.date_object()
        return model.objects.create(**data, **kwargs)

    def test_010_is_admin_superuser(self):
        admin = self.create_user(Admin, is_superuser=True)
        self.request.user = admin
        self.assertTrue(IsAdminSuperUserPerm().has_permission(self.request, self.view))
        admin_user = self.create_user(Admin)
        self.request.user = admin_user
        self.assertFalse(IsAdminSuperUserPerm().has_permission(self.request, self.view))

    def test_020_is_company_superuser(self):
        company_superuser = self.create_user(CompanyUser, is_superuser=True)
        self.request.user = company_superuser
        self.assertTrue(IsCompanySuperUserPerm().has_permission(self.request, self.view))
        company_user = self.create_user(CompanyUser)
        self.request.user = company_user
        self.assertFalse(IsCompanySuperUserPerm().has_permission(self.request, self.view))

    def test_030_scope_permissions(self):
        company_user = self.create_user(CompanyUser)
        admin_user = self.create_user(Admin)
        customer = self.create_user(CustomerUser)
        ScopeTuple = namedtuple("ScopeTuple", ["user", "perm"])
        scopes = [
            ScopeTuple(company_user, IsCompanyScopeUserPerm),
            ScopeTuple(admin_user, IsAdminScopeUserPerm),
            ScopeTuple(customer, IsCustomerScopeUserPerm),
        ]
        for pos1, scope1 in enumerate(scopes):
            for pos2, scope2 in enumerate(scopes):
                self.request.user = scope1.user
                if pos2 == pos1:
                    self.assertTrue(scope2.perm().has_permission(self.request, self.view))
                else:
                    self.assertFalse(scope2.perm().has_permission(self.request, self.view))

    def test_040_company_permissions(self):
        company_owner = self.create_user(CompanyUser)
        company = Company.objects.create(
            created_by=company_owner,
            title=self.faker.word(),
            email=self.faker.email(),
        )
        company_owner.company = company
        company_owner.save()
        company_user = self.create_user(CompanyUser)
        company_user.company = company
        company_user.save()
        self.request.user = company_owner
        self.assertTrue(CompanyOwnerPerm().has_permission(self.request, self.view))
        self.assertFalse(CompanyEmployeePerm().has_permission(self.request, self.view))
        self.request.user = company_user
        self.assertFalse(CompanyOwnerPerm().has_permission(self.request, self.view))
        self.assertTrue(CompanyEmployeePerm().has_permission(self.request, self.view))

    def test_050_admin_perm_check(self):
        admin = self.create_user(Admin)
        admin.user_permissions.create(
            name="user_permission",
            codename="up",
        )

        group = AdminGroup.objects.create(
            name="admin_group",
        )
        group.permission.create(
            name="group_permission",
            codename="gp",
        )
        admin.groups.add(group)

        self.request.user = admin

        self.assertTrue(UserPermissionCheck("up").has_permission(self.request, self.view))
        self.assertFalse(UserPermissionCheck("not_exists").has_permission(self.request, self.view))
        self.assertTrue(UserPermissionCheck("gp").has_permission(self.request, self.view))

        admin.groups.remove(group)

        self.assertFalse(UserPermissionCheck("gp").has_permission(self.request, self.view))

        dev_group = DeveloperGroup.objects.create(name="dev_group")
        dev_group.permission.create(
            name="company_group_perm",
            codename="cgp",
        )
        dev_perm = DeveloperPermission.objects.create(
            name="developer_perm",
            codename="dp",
        )

        self.assertFalse(UserPermissionCheck("dp").has_permission(self.request, self.view))
        self.assertFalse(UserPermissionCheck("cgp").has_permission(self.request, self.view))

        admin.developer_permissions.add(dev_perm)
        admin.developer_groups.add(dev_group)
        self.assertTrue(UserPermissionCheck("dp").has_permission(self.request, self.view))
        self.assertTrue(UserPermissionCheck("cgp").has_permission(self.request, self.view))

    def test_060_dev_perm_check(self):
        company_user = self.create_user(CompanyUser)
        self.request.user = company_user
        self.assertFalse(UserPermissionCheck("cup").has_permission(self.request, self.view))

        company_user.user_permissions.create(
            name="company_user_perm",
            codename="cup",
        )

        self.assertTrue(UserPermissionCheck("cup").has_permission(self.request, self.view))

        company_user.user_permissions.remove(DeveloperPermission.objects.get(codename="cup"))

        self.assertFalse(UserPermissionCheck("cup").has_permission(self.request, self.view))

        group = DeveloperGroup.objects.create(
            name="cgroup",
        )
        group.permission.create(
            name="company_group_perm",
            codename="cgp",
        )

        self.assertFalse(UserPermissionCheck("cgp").has_permission(self.request, self.view))

        company_user.groups.add(group)
        self.assertTrue(UserPermissionCheck("cgp").has_permission(self.request, self.view))

    def test_070_customer_perm_check(self):
        customer_user = self.create_user(CustomerUser)
        self.request.user = customer_user
        self.assertFalse(UserPermissionCheck("perm").has_permission(self.request, self.view))
