from administrator.models import Admin
from base.validators import AbstractUserVerify
from customer.models import CustomerUser
from developer.models import CompanyUser, Company


class IsActiveUserVerify(AbstractUserVerify):
    def _verify(self, user):
        return user.is_active


class NotBannedUserVerify(AbstractUserVerify):
    def _verify(self, user):
        return not user.is_banned


class IsAdminSuperUserVerify(AbstractUserVerify):
    def _verify(self, user):
        if isinstance(user, Admin):
            return user.is_superuser
        return False


class IsCompanySuperUserVerify(AbstractUserVerify):
    def _verify(self, user):
        if isinstance(user, CompanyUser):
            return user.is_superuser
        return False


class AdminScopeUserVerify(AbstractUserVerify):
    def _verify(self, user) -> bool:
        return isinstance(user, Admin)


class CompanyScopeUserVerify(AbstractUserVerify):
    def _verify(self, user) -> bool:
        return isinstance(user, CompanyUser)


class CustomerScopeUserVerify(AbstractUserVerify):
    def _verify(self, user) -> bool:
        return isinstance(user, CustomerUser)


class CompanyOwnerVerify(AbstractUserVerify):
    def _verify(self, user) -> bool:
        if isinstance(user, CompanyUser):
            return Company.objects.filter(created_by=user).exists()
        return False


class CompanyEmployeeVerify(AbstractUserVerify):
    def _verify(self, user):
        if isinstance(user, CompanyUser):
            if user.company:
                return user.company.created_by != user
        return False
