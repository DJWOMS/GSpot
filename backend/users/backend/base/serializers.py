from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from rest_framework.fields import ValidationError
from rest_framework.serializers import ModelSerializer
from common.permissions.validators import ActiveUserValidator, BannedUserValidatorVerify
from base.models import BaseAbstractUser, BasePermission, BaseGroup


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
