from base.views import PersonalAccount
from developer.models import CompanyUser

from developer.serializers import account_serializers
from rest_framework.permissions import AllowAny


class DeveloperAccountViewSet(PersonalAccount):
    queryset = CompanyUser.objects.all()

    serializer_map = {
        'default': account_serializers.DeveloperAccountRetrieveSerializers,
        'retrieve': account_serializers.DeveloperAccountRetrieveSerializers,
        'update': account_serializers.DeveloperAccountUpdateSerializers,
        'partial_update': account_serializers.DeveloperAccountUpdateSerializers,
        'destroy': account_serializers.DeveloperAccountRetrieveSerializers,
    }

    permission_map = {
        'default': [AllowAny],
        'retrieve': [AllowAny],
        'update': [AllowAny],
        'partial_update': [AllowAny],
        'destroy': [AllowAny],
    }


class DeveloperChangePasswordViewSet(PersonalAccount):
    queryset = CompanyUser.objects.all()

    serializer_map = {
        'default': account_serializers.DeveloperChangePasswordRetUpdSerializers,
        'retrieve': account_serializers.DeveloperChangePasswordRetUpdSerializers,
        'partial_update': account_serializers.DeveloperChangePasswordRetUpdSerializers,
    }

    permission_map = {
        'default': [AllowAny],
        'retrieve': [AllowAny],
        'partial_update': [AllowAny],
    }
