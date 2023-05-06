from administrator.models import AdminPermission
from common.management import BasePermissionCreatingCommand


class Command(BasePermissionCreatingCommand):
    @staticmethod
    def get_permission_model():
        return AdminPermission
