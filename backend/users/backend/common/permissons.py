from base.permissions import BaseUserPermissions
from common import validators


class IsSuperUser(BaseUserPermissions, validators.IsSuperUser):
    """Check Super User Permission"""


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
