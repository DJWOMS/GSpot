from administrator.models import Admin
from base.validators import AbstractUserVerify
from customer.models import CustomerUser
from developer.models import Company, CompanyUser


class IsActiveUserVerify(AbstractUserVerify):
    def verify(self, user):
        return user.is_active


class NotBannedUserVerify(AbstractUserVerify):
    def verify(self, user):
        return not user.is_banned


class IsAdminSuperUserVerify(AbstractUserVerify):
    def verify(self, user):
        if isinstance(user, Admin):
            return user.is_superuser
        return False


class IsCompanySuperUserVerify(AbstractUserVerify):
    def verify(self, user):
        if isinstance(user, CompanyUser):
            return user.is_superuser
        return False


class AdminScopeUserVerify(AbstractUserVerify):
    def verify(self, user) -> bool:
        return isinstance(user, Admin)


class CompanyScopeUserVerify(AbstractUserVerify):
    def verify(self, user) -> bool:
        return isinstance(user, CompanyUser)


class CustomerScopeUserVerify(AbstractUserVerify):
    def verify(self, user) -> bool:
        return isinstance(user, CustomerUser)


class CompanyOwnerVerify(AbstractUserVerify):
    def verify(self, user) -> bool:
        if isinstance(user, CompanyUser):
            return user.is_superuser or Company.objects.filter(created_by=user).exists()
        return False


class CompanyEmployeeVerify(AbstractUserVerify):
    def verify(self, user):
        if isinstance(user, CompanyUser):
            if user.company:
                return user.company.created_by != user
        return False
