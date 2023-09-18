from base.validators import AbstractUserVerify
from rest_framework.permissions import BasePermission


class BaseUserPermissions(AbstractUserVerify, BasePermission):
    def has_permission(self, request, view):
        return self.verify(request.user)
