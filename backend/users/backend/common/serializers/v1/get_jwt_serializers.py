import os
from rest_framework import serializers
from common.services.jwt.token import Token
from common.services.jwt.exceptions import UnauthorizedUserError, TokenBannedError
from django.conf import settings


class GetJwtSerializers(serializers.Serializer):
    refresh_token = serializers.CharField()

    def validate(self, attrs):
        token = Token()
        user = self.context["request"].user
        refresh_token = attrs.pop('refresh_token')
        token_in_black_list = False
        if token.check_token(refresh_token):
            if not token_in_black_list:
                if user.is_active and not user.is_banned:
                    exp_left = token.check_exp_left(refresh_token)
                    attrs['user'] = user
                    print(settings.REFRESH_TOKEN_ROTATE_MIN_LIFETIME)
                    if exp_left > int(settings.REFRESH_TOKEN_ROTATE_MIN_LIFETIME.timestamp()):
                        attrs['exp_left'] = True
                        return attrs
                    # - ban refresh token
                    attrs['exp_left'] = False
                    return attrs
                raise UnauthorizedUserError
            else:
                raise TokenBannedError


class ResponseGetJwtSerializers(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()
