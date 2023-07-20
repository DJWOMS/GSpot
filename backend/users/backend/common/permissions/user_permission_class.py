from rest_framework.permissions import IsAuthenticated


class UserPermissionClass:
    @staticmethod
    def get_permission_map() -> dict:
        permission_map = {
            "default": [IsAuthenticated],
            "retrieve": [IsAuthenticated],
            "partial_update": [IsAuthenticated],
            "destroy": [IsAuthenticated],
        }

        return permission_map
