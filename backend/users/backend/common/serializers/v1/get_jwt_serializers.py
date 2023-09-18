from base.exceptions import AuthenticationFailed
from common.permissions.verifiers import IsActiveUserVerify, NotBannedUserVerify
from common.services.jwt.token import Token
from django.conf import settings
from rest_framework import serializers


class GetJwtSerializers(serializers.Serializer):
    refresh_token = serializers.CharField()

    def validate(self, attrs):
        user = self.context["request"].user
        refresh_token = attrs.get("refresh_token")
        token_in_black_list = False
        Token().check_token(refresh_token)
        if token_in_black_list:
            raise AuthenticationFailed("TokenBannedError")
        if not IsActiveUserVerify().verify(user=user):
            raise AuthenticationFailed("UserIsNotActive")
        if not NotBannedUserVerify().verify(user=user):
            raise AuthenticationFailed("UserIsBanned")
        attrs["user"] = user
        return attrs


class ResponseGetJwtSerializers(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()
