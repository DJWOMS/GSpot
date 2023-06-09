from rest_framework import serializers

from administrator.models import Admin
from base.serializers import ChangePasswordSerializers


class AccountRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        ref_name = 'admin_account_retrieve'
        model = Admin
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
        )


class AccountUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        ref_name = 'admin_account_update'
        model = Admin
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'avatar', 'country')


class ChangePasswordRetUpdSerializers(ChangePasswordSerializers):
    class Meta:
        ref_name = 'admin_account_change_pass'
        model = Admin
        fields = ('old_password', 'new_password', 'confirmation_new_password')
