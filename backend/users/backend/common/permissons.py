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
