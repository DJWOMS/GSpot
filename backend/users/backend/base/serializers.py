from base.models import BaseAbstractUser, BaseGroup, BasePermission
from common.permissions.validators import ActiveUserValidator, BannedUserValidatorVerify
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ParseError
from rest_framework.fields import ValidationError
from rest_framework.serializers import ModelSerializer


class BasePermissionSerializer(ModelSerializer):
    class Meta:
        model = BasePermission
        fields = ["name", "codename"]
        abstract = True


class BaseGroupSerializer(ModelSerializer):
    class Meta:
        model = BaseGroup
        fields = ["name", "permission"]
        abstract = True


class ChangePasswordSerializers(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    confirmation_new_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = self.context["request"].user
        old_password = attrs.pop("old_password")
        if not user.check_password(old_password):
            raise ParseError("Please check that your current password is correct")
        self.valid_confirm_password(attrs)
        return attrs

    def validate_new_password(self, value):
        validate_password(value)
        return value

    @staticmethod
    def valid_confirm_password(attrs):
        new_password = attrs.get("new_password")
        confirmation_new_password = attrs.get("confirmation_new_password")
        if not new_password == confirmation_new_password:
            raise ParseError("The confirmation password does not match the new password")
        return attrs

    def create(self, validate_data):
        password = validate_data.pop("new_password")
        instance = self.context["request"].user
        instance.set_password(password)
        instance.save()
        return instance


class BaseAuthSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    def validate(self, attrs):
        if not self.Meta.model.objects.filter(email=attrs["email"]).exists():
            raise ValidationError(_("Email or Password not valid"))
        user = self.Meta.model.objects.get(email=attrs["email"])

        if not user.check_password(attrs["password"]):
            raise ValidationError(_("Email or Password not valid"))
        ActiveUserValidator(_("Inactive user")).validate(user)
        BannedUserValidatorVerify(_("User is banned")).validate(user)
        attrs["user"] = user
        return attrs

    class Meta:
        model: BaseAbstractUser
        fields = ("email", "password")


class AuthTokensResponseSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()
