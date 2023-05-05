from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny

from administrator.models import Admin
from administrator.serializers.employee_crud import (
    EmployeeListSerializer,
    EmployeeCreateSerializer,
    EmployeeRetrieveSerializer,
)


class EmployeeListView(generics.ListCreateAPIView):
    queryset = Admin.objects.filter(is_superuser=False)
    permission_classes = [
        AllowAny,
    ]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EmployeeListSerializer
        elif self.request.method == 'POST':
            return EmployeeCreateSerializer


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Admin.objects.filter(is_superuser=False)
    permission_classes = [
        AllowAny,
    ]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EmployeeRetrieveSerializer

    '''
    def get_serializer(self, instance, **kwargs):
        if self.request.method == 'GET':
            return EmployeeRetrieveSerializer(instance=instance)
    '''
