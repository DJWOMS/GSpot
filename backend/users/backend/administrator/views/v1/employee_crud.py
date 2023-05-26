from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from administrator.models import Admin
from administrator.serializers.v1.employee_crud import (
    EmployeeListSerializer,
    EmployeeCreateUpdateSerializer,
    EmployeeRetrieveSerializer,
    EmployeeSendEmailSerializer,
)
from common.permissions.permissons import IsAdminSuperUserPerm


class EmployeeListView(generics.ListCreateAPIView):
    queryset = Admin.objects.filter(is_superuser=False)
    permission_classes = [
        IsAdminSuperUserPerm,
    ]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EmployeeListSerializer
        elif self.request.method == 'POST':
            return EmployeeCreateUpdateSerializer


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Admin.objects.filter(is_superuser=False)
    permission_classes = [
        IsAdminSuperUserPerm,
    ]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EmployeeRetrieveSerializer
        elif self.request.method == 'PUT':
            return EmployeeCreateUpdateSerializer
        elif self.request.method == 'PATCH':
            return EmployeeCreateUpdateSerializer


class EmployeeSendEmail(APIView):
    permission_classes = [
        IsAdminSuperUserPerm,
    ]

    serializer_class = EmployeeSendEmailSerializer

    def post(self, request, pk):
        admin = Admin.objects.get(pk=pk, is_active=False)
        serializer = self.serializer_class(instance=admin, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        """send totp"""
        return Response(serializer.data, status=status.HTTP_200_OK)
