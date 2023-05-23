from rest_framework.permissions import BasePermission

from base.validators import AbstractUserVerify


class BaseUserPermissions(AbstractUserVerify, BasePermission):
    def has_permission(self, request, view):
        return self._verify(request.user)
