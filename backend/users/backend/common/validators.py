from administrator.models import Admin
from base.validators import VerificationError, BaseUserValidation, AbstractUserVerify
from customer.models import CustomerUser
from developer.models import CompanyUser, Company


class IsActiveUser(AbstractUserVerify):
    def verify(self, user):
        return user.is_active


class NotBannedUser(AbstractUserVerify):
    def verify(self, user):
        return not user.is_banned


class IsAdminSuperUser(AbstractUserVerify):
    def verify(self, user):
        if isinstance(user, Admin):
            return user.is_superuser
        return False


class IsCompanySuperUser(AbstractUserVerify):
    def verify(self, user):
        if isinstance(user, CompanyUser):
            return user.is_superuser
        return False


class AdminScopeUser(AbstractUserVerify):
    def verify(self, user) -> bool:
        return isinstance(user, Admin)


class CompanyScopeUser(AbstractUserVerify):
    def verify(self, user) -> bool:
        return isinstance(user, CompanyUser)


class CustomerScopeUser(AbstractUserVerify):
    def verify(self, user) -> bool:
        return isinstance(user, CustomerUser)


class CompanyOwner(AbstractUserVerify):
    def verify(self, user) -> bool:
        if isinstance(user, CompanyUser):
            return Company.objects.filter(created_by=user).exists()
        return False


class CompanyEmployee(AbstractUserVerify):
    def verify(self, user):
        if isinstance(user, CompanyUser):
            if user.company:
                return user.company.created_by != user
        return False


class NotActiveUserError(VerificationError):
    message = 'not active user'


class ActiveUserVerify(BaseUserValidation, IsActiveUser):
    """User Active Verification"""

    exception = NotActiveUserError


class BannedUserError(VerificationError):
    message = 'user is  banned'


class BannedUserVerify(BaseUserValidation, NotBannedUser):
    """Banned User Verification"""

    exception = BannedUserError
