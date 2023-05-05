from rest_framework import generics
from rest_framework.permissions import AllowAny

from administrator.models import Admin
from administrator.serializers.v1.employee_crud import (
    EmployeeListSerializer,
    EmployeeCreateUpdateSerializer,
    EmployeeRetrieveSerializer,
    EmployeePermissionsSerializer,
)


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


class EmployeePermissionsView(generics.RetrieveAPIView, generics.UpdateAPIView):
    queryset = Admin.objects.filter(is_superuser=False)
    serializer_class = EmployeePermissionsSerializer
    permission_classes = [AllowAny]
