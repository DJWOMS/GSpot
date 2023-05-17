from rest_framework import generics
from common.permissons import CompanyOwner
from developer.models import CompanyUser
from developer.serializers.v1.employee_crud import (
    DeveloperEmployeeListSerializer,
    DeveloperEmployeeCreateSerializer,
)


class DeveloperEmployeeListView(generics.ListCreateAPIView):
    permission_classes = [CompanyOwner]

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
            return DeveloperEmployeeCreateSerializer


class DeveloperEmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CompanyOwner]
