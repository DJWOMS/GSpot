from rest_framework import generics
from rest_framework.permissions import AllowAny

from administrator.models import Admin
from developer.models import CompanyUser
from developer.serializers.v1.employee_crud import (
    DeveloperEmployeeListSerializer,
    DeveloperEmployeeCreateSerializer,
)


class DeveloperEmployeeListView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]

    def get_queryset(self):
        if isinstance(self.request.user, CompanyUser):
            return CompanyUser.objects.filter(company=self.request.user.company_owner).exclude(
                id=self.request.user.id
            )
        if isinstance(self.request.user, Admin):
            return CompanyUser.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DeveloperEmployeeListSerializer
        elif self.request.method == 'POST':
            return DeveloperEmployeeCreateSerializer
