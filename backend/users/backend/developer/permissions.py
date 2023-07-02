from common.permissions.permissons import CompanyOwnerPerm
from developer.models import Company, CompanyUser


class CompanyOwnerEmployeePerm(CompanyOwnerPerm):
    def has_object_permission(self, request, view, obj: CompanyUser):
        return obj.company == Company.objects.get(created_by=request.user)
