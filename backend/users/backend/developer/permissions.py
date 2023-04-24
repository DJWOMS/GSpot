from rest_framework.permissions import BasePermission


class IsAdminOrOwnerCompany(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user or request.user.is_staff


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff
