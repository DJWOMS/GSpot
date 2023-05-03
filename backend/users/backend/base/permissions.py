from rest_framework.permissions import BasePermission

from base.validators import AbstractUserVerify


class BaseUserPermissions(BasePermission, AbstractUserVerify):
    def has_permission(self, request, view):
        return self.verify(request.user)
