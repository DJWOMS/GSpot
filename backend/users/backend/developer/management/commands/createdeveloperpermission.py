from base.management.commands.createbasepermission import BasePermissionCreatingCommand
from developer.models import DeveloperPermission


class Command(BasePermissionCreatingCommand):
    @staticmethod
    def get_permission_model():
        return DeveloperPermission
