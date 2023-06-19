from rest_framework import viewsets, generics
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated

from common.permissions.permissons import IsAdminSuperUserPerm


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


class BaseAccountViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        '''
        Метод возвращает сериализатор в зависимости от HTTP метода запроса
        '''
        assert self.serializer_map is not None, (
            "'%s' должен либо включать атрибут `serializer_map`, "
            "или переопределить метод `get_serializer_class()`."
            % self.__class__.__name__
        )
        return self.serializer_map.get(self.request.method)

    def get_object(self):
        '''
        Метод возвращает модель юзера
        '''
        assert self.model is not None, (
            "'%s' должен либо включать атрибут `model`, "
            "или переопределить метод `get_object()`."
            % self.__class__.__name__
        )
        object_ = self.request.user
        if isinstance(object_, self.model):
            return object_
        raise NotFound()


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
