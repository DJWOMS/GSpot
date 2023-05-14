from base.views import PersonalAccount
from customer.serializers import account_serializers
from customer.models import CustomerUser
from rest_framework.permissions import AllowAny


class CustomerAccountViewSet(PersonalAccount):
    queryset = CustomerUser.objects.all()

    serializer_map = {
        'default': account_serializers.CustomerAccountRetrieveSerializers,
        'retrieve': account_serializers.CustomerAccountRetrieveSerializers,
        'update': account_serializers.CustomerAccountUpdateSerializers,
        'partial_update': account_serializers.CustomerAccountUpdateSerializers,
        'destroy': account_serializers.CustomerAccountRetrieveSerializers,
    }

    permission_map = {
        'default': [AllowAny],
        'retrieve': [AllowAny],
        'update': [AllowAny],
        'partial_update': [AllowAny],
        'destroy': [AllowAny],
    }


class CustomerChangePasswordViewSet(PersonalAccount):
    queryset = CustomerUser.objects.all()

    serializer_map = {
        'default': account_serializers.CustomerChangePasswordRetUpdSerializers,
        'retrieve': account_serializers.CustomerChangePasswordRetUpdSerializers,
        'partial_update': account_serializers.CustomerChangePasswordRetUpdSerializers,
    }

    permission_map = {
        'default': [AllowAny],
        'retrieve': [AllowAny],
        'partial_update': [AllowAny],
    }
