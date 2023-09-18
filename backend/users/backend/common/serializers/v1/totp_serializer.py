from common.services.totp.model_factory import db_model_factory
from common.services.totp.totp import TOTPToken
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from rest_framework import serializers


class CheckTOTPSerializer(serializers.Serializer):
    totp_token = serializers.CharField(write_only=True)
    user = serializers.DictField(read_only=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs: dict):
        totp_token = attrs.pop("totp_token")
        totp_data = TOTPToken().check_totp(totp_token)
        model, serializer = db_model_factory.get_models(totp_data['role'])
        user = get_object_or_404(model, id=totp_data['user_id'])
        attrs['user_instance'] = user
        attrs['user_serializer'] = serializer(user)
        attrs['user'] = serializer(user).data
        return attrs

    def save(self, **kwargs):
        password = self.validated_data.pop('password')
        user = self.validated_data['user_instance']
        user.password = make_password(password)
        user.is_active = True
        user.save()
        serializer = self.validated_data['user_serializer']
        self.validated_data['user'] = serializer.data
        return self.validated_data["user"]
