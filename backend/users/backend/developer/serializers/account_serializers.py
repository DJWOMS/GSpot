from rest_framework import serializers
from developer.models import CompanyUser
from base.serializers import ChangePasswordRetUpdSerializers


class DeveloperAccountRetrieveSerializers(serializers.ModelSerializer):

    class Meta:
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


class DeveloperAccountUpdateSerializers(serializers.ModelSerializer):

    class Meta:
        model = CompanyUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'avatar', 'country')


class DeveloperChangePasswordRetUpdSerializers(ChangePasswordRetUpdSerializers):

    class Meta:
        model = CompanyUser
        fields = ('old_password', 'new_password', 'confirmation_new_password')