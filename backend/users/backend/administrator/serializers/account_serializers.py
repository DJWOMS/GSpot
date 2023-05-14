from rest_framework import serializers

from administrator.models import Admin
from base.serializers import ChangePasswordRetUpdSerializers


class AdministratorAccountRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
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


class AdministratorAccountUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'avatar', 'country')


class AdministratorChangePasswordRetUpdSerializers(ChangePasswordRetUpdSerializers):
    class Meta:
        model = Admin
        fields = ('old_password', 'new_password', 'confirmation_new_password')
