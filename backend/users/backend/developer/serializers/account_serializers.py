from rest_framework import serializers
from developer.models import CompanyUser
from base.serializers import ChangePasswordSerializers


class AccountRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        ref_name = 'developer_account_retrieve'
        model = CompanyUser
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
            'company',
        )


class AccountUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        ref_name = 'developer_account_update'
        model = CompanyUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'avatar', 'country')


class ChangePasswordRetUpdSerializers(ChangePasswordSerializers):
    class Meta:
        ref_name = 'developer_account_change_pass'
        model = CompanyUser
        fields = ('old_password', 'new_password', 'confirmation_new_password')
