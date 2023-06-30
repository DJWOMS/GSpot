from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from base.models import BaseAbstractUser
from common.services.totp.totp import TOTPToken
from common.services.totp.model_factory import db_model_factory


class UserTOTPSerializer(serializers.Serializer):
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    is_staff = serializers.BooleanField()
    is_active = serializers.BooleanField()


class CheckTOTPSerializer(serializers.Serializer):
    totp_token = serializers.CharField()
    user = UserTOTPSerializer(read_only=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs: dict):
        totp_token = attrs.get('totp_token')
        data = TOTPToken().check_totp(totp_token)
        if data is None:
            raise serializers.ValidationError('Current TOTP is not exists.')
        user_model = db_model_factory.get_model(data.get('role'))
        user = user_model.objects.get(id = data.get('user_id'))
        self.instance = user
        attrs['user'] = UserTOTPSerializer(user).data
        return attrs
    
    def update(self, user, validated_data):
        # if not isinstance(user, BaseAbstractUser):
        #     raise TypeError('Object must will be the "BaseAbstractUser" instance required!')
        password = self.validated_data.pop('password')
        user.password = make_password(password)
        user.is_active = True
        user.save()
        self.validated_data['user'] = UserTOTPSerializer(user).data
        return user
