from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from common.models import Country, ContactType
from common.serializers.serializers import CountrySerializer, ContactTypeSerializer
from common.permissons import IsAdminSuperUser


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAdminSuperUser]

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminSuperUser]
        return [permission() for permission in permission_classes]


class ContactTypeViewSet(viewsets.ModelViewSet):
    queryset = ContactType.objects.all()
    serializer_class = ContactTypeSerializer
    permission_classes = [IsAdminSuperUser]

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminSuperUser]
        return [permission() for permission in permission_classes]
