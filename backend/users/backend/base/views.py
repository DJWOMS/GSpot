from common.permissions.permissons import IsAdminSuperUserPerm
from rest_framework import generics, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated


class BaseAdminSuperUserViewSet(viewsets.ModelViewSet):
    """Base class, where list, retrieve have the permissions - IsAuthenticated,
    other methods have the permission - IsAdminSuperUser"""

    queryset = None
    serializer_class = None
    permission_classes = [IsAdminSuperUserPerm]
    http_method_names = ["get", "retrieve", "post", "put", "delete"]

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = self.permission_classes
        return [permission() for permission in permission_classes]


class PartialUpdateMixin:
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class PersonalAccount(viewsets.ModelViewSet):
    def get_serializer_class(self):
        return self.serializer_map.get(self.action, self.serializer_map["default"])

    def get_permissions(self):
        return [
            permission()
            for permission in self.permission_map.get(self.action, self.permission_map["default"])
        ]

    def get_object(self):
        obj = self.request.user
        if obj.is_anonymous:
            raise NotFound()
        self.check_object_permissions(self.request, obj)
        return obj
