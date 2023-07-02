from base.models import BaseAbstractUser
from common.services.totp.model_factory import db_model_factory
from common.services.totp.totp import TOTPToken
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from rest_framework import serializers


class UserTOTPSerializer(serializers.Serializer):
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    is_staff = serializers.BooleanField()
    is_active = serializers.BooleanField()


class CheckTOTPSerializer(serializers.Serializer):
    totp_token = serializers.CharField(write_only=True)
    user = UserTOTPSerializer(read_only=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs: dict):
        totp_token = attrs.pop("totp_token")
        totp_data = TOTPToken().check_totp(totp_token)
        user_model = db_model_factory.get_model(totp_data["role"])
        user = get_object_or_404(user_model, id=totp_data["user_id"])
        attrs["user"] = user
        return attrs

    def save(self, **kwargs):
        password = self.validated_data.pop("password")
        user = self.validated_data["user"]
        user.password = make_password(password)
        user.is_active = True
        user.save()
        return self.validated_data["user"]
