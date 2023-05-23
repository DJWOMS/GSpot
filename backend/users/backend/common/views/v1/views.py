from rest_framework import viewsets

from base.views.base_views import BaseAdminSuperUserViewSet

from common.models import Country, ContactType
from common.serializers.v1.contenttype_serializer import ContactTypeSerializer
from common.serializers.v1.country_serializer import CountrySerializer


class CountryViewSet(BaseAdminSuperUserViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class ContactTypeViewSet(viewsets.ModelViewSet):
    queryset = ContactType.objects.all()
    serializer_class = ContactTypeSerializer
