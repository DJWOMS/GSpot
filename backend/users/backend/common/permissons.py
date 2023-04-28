from rest_framework.permissions import BasePermission

from base.permissions import BaseUserPermissions
from common import validators


class IsAdminSuperUser(BaseUserPermissions, validators.IsAdminSuperUser):
    """Check Admin Super User Permission"""


class IsCompanySuperUser(BaseUserPermissions, validators.IsCompanySuperUser):
    """Check Admin Super User Permission"""


class IsAdminScopeUser(BaseUserPermissions, validators.AdminScopeUser):
    """Check Admin User"""


class IsCompanyScopeUser(BaseUserPermissions, validators.CompanyScopeUser):
    """Check Company User """


class IsCustomerScopeUser(BaseUserPermissions, validators.CustomerScopeUser):
    """Check Customer User """


class CompanyOwner(BaseUserPermissions, validators.CompanyOwner):
    """Check Company Owner"""


class CompanyEmployee(BaseUserPermissions, validators.CompanyEmployee):
    """Check Company Employee"""


class UserPermissionCheck(BasePermission):

    def __init__(self, permission: str):
        self.permission = permission

    def __call__(self, *args, **kwargs):
        return self

    def has_permission(self, request, view):
        return request.user.has_perm(self.permission)
