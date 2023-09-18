from administrator.models import Admin
from base.permissions import BaseUserPermissions
from common.permissions import verifiers
from common.permissions.verifiers import IsAdminSuperUserVerify
from developer.models import CompanyUser
from rest_framework.permissions import BasePermission


class IsAdminSuperUserPerm(BaseUserPermissions, IsAdminSuperUserVerify):
    """Check Admin Super User Permission"""


class IsCompanySuperUserPerm(BaseUserPermissions, verifiers.IsCompanySuperUserVerify):
    """Check Admin Super User Permission"""


class IsAdminScopeUserPerm(BaseUserPermissions, verifiers.AdminScopeUserVerify):
    """Check Admin User"""


class IsCompanyScopeUserPerm(BaseUserPermissions, verifiers.CompanyScopeUserVerify):
    """Check Company User"""


class IsCustomerScopeUserPerm(BaseUserPermissions, verifiers.CustomerScopeUserVerify):
    """Check Customer User"""


class CompanyOwnerPerm(BaseUserPermissions, verifiers.CompanyOwnerVerify):
    """Check Company Owner"""


class CompanyEmployeePerm(BaseUserPermissions, verifiers.CompanyEmployeeVerify):
    """Check Company Employee"""


class UserPermissionCheck(BasePermission):
    def __init__(self, codename: str):
        self.codename = codename

    def __call__(self, *args, **kwargs):
        return self

    def has_permission(self, request, view):
        if isinstance(request.user, (Admin, CompanyUser)):
            return request.user.has_perm(self.codename)
        return False
