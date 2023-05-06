from developer.models import DeveloperPermission
from common.management import BasePermissionCreatingCommand


class Command(BasePermissionCreatingCommand):
    @staticmethod
    def get_permission_model():
        return DeveloperPermission
