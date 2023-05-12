from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ParseError
from rest_framework.serializers import ModelSerializer
from base.models import BasePermission, BaseGroup


class BasePermissionSerializer(ModelSerializer):
    class Meta:
        model = BasePermission
        fields = ['name', 'codename']
        abstract = True


class BaseGroupSerializer(ModelSerializer):
    class Meta:
        model = BaseGroup
        fields = ['name', 'permission']
        abstract = True


class ChangePasswordRetUpdSerializers(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    confirmation_new_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = self.instance
        old_password = attrs.pop('old_password')
        if not user.check_password(old_password):
            raise ParseError(
                'Please check that your current password is correct'
            )
        self.valid_confirm_password(attrs)
        return attrs

    def validate_new_password(self, value):
        validate_password(value)
        return value

    @staticmethod
    def valid_confirm_password(attrs):
        new_password = attrs.get('new_password')
        confirmation_new_password = attrs.get('confirmation_new_password')
        if not new_password == confirmation_new_password:
            raise ParseError(
                'The confirmation password does not match the new password'
            )
        return attrs

    def update(self, instance, validate_data):
        password = validate_data.pop('new_password')
        instance.set_password(password)
        instance.save()
        return instance
