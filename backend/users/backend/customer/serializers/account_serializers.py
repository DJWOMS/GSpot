from rest_framework import serializers

from customer.models import CustomerUser
from base.serializers import ChangePasswordSerializers


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = ('id', 'username')


class AccountRetrieveSerializers(serializers.ModelSerializer):
    friends = UserSerializers(many=True)

    class Meta:
        ref_name = 'customer_account_retrieve'
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


class AccountUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        ref_name = 'customer_account_update'
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


class ChangePasswordRetUpdSerializers(ChangePasswordSerializers):
    class Meta:
        ref_name = 'customer_account_change_pass'
        model = CustomerUser
        fields = ('old_password', 'new_password', 'confirmation_new_password')
