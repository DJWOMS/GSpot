from rest_framework.permissions import BasePermission

from common.permissions.permissons import CompanyOwnerPerm
from developer.models import CompanyUser, Company


class IsAdminOrOwnerCompany(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user or request.user.is_staff


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


class CompanyOwnerEmployeePerm(CompanyOwnerPerm):
    def has_object_permission(self, request, view, obj: CompanyUser):
        return obj.company == Company.objects.get(created_by=request.user)
