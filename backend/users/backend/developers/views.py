from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import CompanyUser, Company
from .permissions import IsAdminOrOwnerCompany, IsAdmin
from .serializers import CompanySerializer, CompanyEmployeeSerializer, CompanyUserSerializer


class CompanyRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompanySerializer
    permission_classes = [IsAdminOrOwnerCompany]

    def get_object(self):
        queryset = Company.objects.filter(created_by=self.request.user)
        obj = generics.get_object_or_404(queryset, pk=self.kwargs["pk"])
        return obj


class CompanyEmployeeListView(generics.ListAPIView):
    serializer_class = CompanySerializer
    permission_classes = [IsAdminOrOwnerCompany]

    def get_queryset(self):
        company_id = self.kwargs['company_id']
        return CompanyUser.objects.filter(company_id=company_id)


class CompanyEmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyEmployeeSerializer

    def get_queryset(self):
        company_id = self.kwargs['company_id']
        company = Company.objects.get(pk=company_id)
        if self.request.user in company.companyuser_set.all():
            return Company.objects.filter(pk=company_id)
        return Company.objects.none()


class CompanyAdminListView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAdmin]


class CompanyAdminDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAdmin]


class CompanyUserViewSet(viewsets.ModelViewSet):
    queryset = CompanyUser.objects.all()
    serializer_class = CompanyUserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
