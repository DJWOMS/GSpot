from base.views import PersonalAccount
from administrator.models import Admin
from administrator.serializers import account_serializers
from rest_framework.permissions import AllowAny


class AccountViewSet(PersonalAccount):
    queryset = Admin.objects.all()

    serializer_map = {
        'default': account_serializers.AccountRetrieveSerializers,
        'retrieve': account_serializers.AccountRetrieveSerializers,
        'update': account_serializers.AccountUpdateSerializers,
        'partial_update': account_serializers.AccountUpdateSerializers,
        'destroy': account_serializers.AccountRetrieveSerializers,
    }

    permission_map = {
        'default': [AllowAny],
        'retrieve': [AllowAny],
        'update': [AllowAny],
        'partial_update': [AllowAny],
        'destroy': [AllowAny],
    }


class ChangePasswordViewSet(PersonalAccount):
    queryset = Admin.objects.all()

    serializer_map = {
        'default': account_serializers.ChangePasswordRetUpdSerializers,
        'retrieve': account_serializers.ChangePasswordRetUpdSerializers,
        'partial_update': account_serializers.ChangePasswordRetUpdSerializers,
    }

    permission_map = {
        'default': [AllowAny],
        'retrieve': [AllowAny],
        'partial_update': [AllowAny],
    }
