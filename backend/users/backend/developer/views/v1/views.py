from rest_framework import viewsets
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
    IsAdminUser,
    AllowAny,
)

from developer.models import CompanyUser, Company, DeveloperGroup, DeveloperPermission
from developer.permissions import IsAdminOrOwnerCompany
from developer.serializers.serializers import (
    CompanySerializer,
    CompanyEmployeeSerializer,
    CompanyUserSerializer,
)
from developer.serializers.v1 import (
    DeveloperGroupSerializer,
    DeveloperPermissionSerializer,
)


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()

    serializer_map = {
        'default': CompanySerializer,
        'list': CompanyEmployeeSerializer,
        'create': CompanySerializer,
        'retrieve': CompanySerializer,
        'update': CompanySerializer,
        'partial_update': CompanySerializer,
        'destroy': CompanySerializer,
        'employees': CompanySerializer,
    }

    permission_map = {
        'default': [AllowAny],
        'list': [IsAuthenticated],
        'create': [AllowAny],
        'retrieve': [IsAuthenticated],
        'update': [IsAdminOrOwnerCompany],
        'partial_update': [IsAdminOrOwnerCompany],
        'destroy': [IsAdminOrOwnerCompany],
        'employees': [IsAdminOrOwnerCompany],
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
            permission_classes = [IsAdminOrOwnerCompany]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class DeveloperGroupViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = DeveloperGroup.objects.all()
    serializer_class = DeveloperGroupSerializer


class DeveloperPermissionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = DeveloperPermission.objects.all()
    serializer_class = DeveloperPermissionSerializer
