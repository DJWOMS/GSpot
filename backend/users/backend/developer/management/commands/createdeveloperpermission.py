from developer.models import DeveloperPermission
from base.management.commands.createbasepermission import BasePermissionCreatingCommand


class Command(BasePermissionCreatingCommand):
    @staticmethod
    def get_permission_model():
        return DeveloperPermission
