from rest_framework import serializers
from common.services.jwt.token import Token
from django.conf import settings

from base.exceptions import AuthenticationFailed


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
                    if exp_left > int(settings.REFRESH_TOKEN_ROTATE_MIN_LIFETIME.total_seconds()):
                        attrs['exp_left'] = True
                        return attrs
                    # - ban refresh token
                    attrs['exp_left'] = False
                    return attrs
                raise AuthenticationFailed('UnauthorizedUserError')
            else:
                raise AuthenticationFailed('TokenBannedError')


class ResponseGetJwtSerializers(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()
