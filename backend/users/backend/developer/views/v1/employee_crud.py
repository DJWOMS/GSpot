from rest_framework import generics

from administrator.serializers.v1.employee_crud import EmployeeCreateUpdateSerializer
from common.permissions.permissons import CompanyOwnerPerm
from developer.models import CompanyUser
from developer.serializers.v1.employee_crud import (
    DeveloperEmployeeListSerializer,
    DeveloperEmployeeDetailSerializer,
    DeveloperEmployeeCreateUpdateSerializer,
)


class DeveloperEmployeeListView(generics.ListCreateAPIView):
    permission_classes = [CompanyOwnerPerm]

    def get_queryset(self):
        return CompanyUser.objects.filter(company=self.request.user.company_owner).exclude(
            id=self.request.user.id
        )

    def perform_create(self, serializer):
        serializer.save(
            company=self.request.user.company,
        )

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DeveloperEmployeeListSerializer
        elif self.request.method == 'POST':
            return DeveloperEmployeeCreateUpdateSerializer


class DeveloperEmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CompanyOwnerPerm]

    def get_queryset(self):
        return CompanyUser.objects.filter(company=self.request.user.company_owner).exclude(
            id=self.request.user.id
        )

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DeveloperEmployeeDetailSerializer
        elif self.request.method == 'PUT':
            return EmployeeCreateUpdateSerializer
        elif self.request.method == 'PATCH':
            return EmployeeCreateUpdateSerializer
