from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from common.permissons import IsAdminSuperUser


class BaseAdminSuperUserViewSet(viewsets.ModelViewSet):
    """Base class, where list, retrieve have the permissions - IsAuthenticated,
    other methods have the permission - IsAdminSuperUser"""

    queryset = None
    serializer_class = None
    permission_classes = [IsAdminSuperUser]
    http_method_names = ["get", "retrieve", "post", "put", "delete"]

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]
