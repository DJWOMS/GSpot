from rest_framework import viewsets
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
    AllowAny,
)

from common.permissons import CompanyOwner, IsCompanySuperUser
from developer.models import CompanyUser, Company
from developer.serializers.serializers import (
    CompanySerializer,
    CompanyEmployeeSerializer,
    CompanyUserSerializer,
)


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()

    serializer_map = {
        'default': CompanySerializer,
        'list': CompanyEmployeeSerializer,
    }

    permission_map = {
        'default': [AllowAny],
        'list': [IsAuthenticated],
        'create': [AllowAny],
        'retrieve': [IsAuthenticated],
        'update': [CompanyOwner, IsCompanySuperUser],
        'partial_update': [CompanyOwner, IsCompanySuperUser],
        'destroy': [CompanyOwner, IsCompanySuperUser],
        'employees': [CompanyOwner, IsCompanySuperUser],
    }

    def get_serializer_class(self):
        return self.serializer_map.get(self.action, self.serializer_map['default'])

    def get_permissions(self):
        return [
            permission()
            for permission in self.permission_map.get(self.action, self.permission_map['default'])
        ]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class CompanyUserViewSet(viewsets.ModelViewSet):
    queryset = CompanyUser.objects.all()
    serializer_class = CompanyUserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsCompanySuperUser, CompanyOwner]
        else:
            permission_classes = [IsCompanySuperUser]
        return [permission() for permission in permission_classes]
