from rest_framework import serializers

from customer.models import CustomerUser
from base.serializers import ChangePasswordRetUpdSerializers


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = ('id', 'username')


class CustomerAccountRetrieveSerializers(serializers.ModelSerializer):
    friends = UserSerializers(many=True)

    class Meta:
        model = CustomerUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone',
            'created_at',
            'update_at',
            'avatar',
            'country',
            'friends',
            'birthday',
        )


class CustomerAccountUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone',
            'avatar',
            'country',
            'birthday',
        )


class CustomerChangePasswordRetUpdSerializers(ChangePasswordRetUpdSerializers):
    class Meta:
        model = CustomerUser
        fields = ('old_password', 'new_password', 'confirmation_new_password')
