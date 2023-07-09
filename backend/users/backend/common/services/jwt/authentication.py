from typing import Type

from base.exceptions import AuthenticationFailed
from base.models import BaseAbstractUser
from common.services.jwt.token import Token
from django.conf import settings
from rest_framework.authentication import BaseAuthentication

from .exceptions import TokenIsNotFoundInDb


class CustomJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        try:
            jwt_token = self.get_token(request)
        except AuthenticationFailed:
            return None

        self.validate_token(jwt_token)
        payload = Token().get_access_data(jwt_token)
        if payload:
            user = self.get_user(payload)
            return user, payload
        else:
            raise TokenIsNotFoundInDb()

    @staticmethod
    def validate_token(token) -> None:
        Token().check_token(token)

    def get_user(self, payload: dict) -> BaseAbstractUser:
        user_id = payload.get("user_id")
        user_role = payload.get("role")
        if not user_id:
            raise AuthenticationFailed("User identifier not found")
        if not user_role:
            raise AuthenticationFailed("User role not found")

        user_model = self.get_user_model(user_role)

        try:
            user = user_model.objects.get(id=user_id)
        except user_model.DoesNotExist:
            raise AuthenticationFailed("User not found")

        return user

    @staticmethod
    def get_user_model(role: str) -> Type[BaseAbstractUser]:
        all_user_models = BaseAbstractUser.__subclasses__()
        for user_model in all_user_models:
            if user_model._meta.app_label == role:
                return user_model

        raise AuthenticationFailed("No such User role")

    def get_token(self, request) -> str:
        if settings.GET_TOKEN_FROM == "header":
            token = self._get_token_from_header(request)
        else:
            token = self._get_token_from_cookies(request)

        if not token:
            raise AuthenticationFailed("Token not found in %s" % settings.GET_TOKEN_FROM)
        return token

    @staticmethod
    def _get_token_from_header(request) -> str:
        token = request.META.get("HTTP_AUTHORIZATION")
        return token

    @staticmethod
    def _get_token_from_cookies(request) -> str:
        token = request.COOKIES.get("Authentication")
        return token
