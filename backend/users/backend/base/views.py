from rest_framework import viewsets
from rest_framework.exceptions import NotFound


class PersonalAccount(viewsets.ModelViewSet):

    def get_serializer_class(self):
        return self.serializer_map.get(self.action, self.serializer_map['default'])

    def get_permissions(self):
        return [
            permission()
            for permission in self.permission_map.get(self.action, self.permission_map['default'])
        ]

    def get_object(self):
        obj = self.request.user
        if obj.is_anonymous:
            raise NotFound()
        self.check_object_permissions(self.request, obj)
        return obj