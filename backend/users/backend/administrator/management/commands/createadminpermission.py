from administrator.models import AdminPermission
from base.management import BasePermissionCreatingCommand


class Command(BasePermissionCreatingCommand):
    @staticmethod
    def get_permission_model():
        return AdminPermission
