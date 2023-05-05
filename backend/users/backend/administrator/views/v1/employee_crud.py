from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny

from administrator.models import Admin
from administrator.serializers.employee_crud import (
    EmployeeListSerializer,
    EmployeeCreateUpdateSerializer,
    EmployeeRetrieveSerializer,
)
from common.permissons import CompanyOwner


class EmployeeListView(generics.ListCreateAPIView):
    queryset = Admin.objects.filter(is_superuser=False)
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EmployeeListSerializer
        elif self.request.method == 'POST':
            return EmployeeCreateUpdateSerializer


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Admin.objects.filter(is_superuser=False)
    permission_classes = [
        AllowAny,
    ]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EmployeeRetrieveSerializer
        elif self.request.method == 'PUT':
            return EmployeeCreateUpdateSerializer
        elif self.request.method == 'PATCH':
            return EmployeeCreateUpdateSerializer
