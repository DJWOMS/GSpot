from base.views import PersonalAccount
from administrator.models import Admin
from administrator.serializers import account_serializers
from rest_framework.permissions import AllowAny


class AdministratorAccountViewSet(PersonalAccount):
    queryset = Admin.objects.all()

    serializer_map = {
        'default': account_serializers.AdministratorAccountRetrieveSerializers,
        'retrieve': account_serializers.AdministratorAccountRetrieveSerializers,
        'update': account_serializers.AdministratorAccountUpdateSerializers,
        'partial_update': account_serializers.AdministratorAccountUpdateSerializers,
        'destroy': account_serializers.AdministratorAccountRetrieveSerializers,
    }

    permission_map = {
        'default': [AllowAny],
        'retrieve': [AllowAny],
        'update': [AllowAny],
        'partial_update': [AllowAny],
        'destroy': [AllowAny],
    }


class AdministratorChangePasswordViewSet(PersonalAccount):
    queryset = Admin.objects.all()

    serializer_map = {
        'default': account_serializers.AdministratorChangePasswordRetUpdSerializers,
        'retrieve': account_serializers.AdministratorChangePasswordRetUpdSerializers,
        'partial_update': account_serializers.AdministratorChangePasswordRetUpdSerializers,
    }

    permission_map = {
        'default': [AllowAny],
        'retrieve': [AllowAny],
        'partial_update': [AllowAny],
    }