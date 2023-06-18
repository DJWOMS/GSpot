from typing import Type

from rest_framework.authentication import BaseAuthentication

from base.exceptions import AuthenticationFailed
from base.models import BaseAbstractUser
from common.services.jwt.request import get_token
from common.services.jwt.token import Token


class CustomJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        try:
            jwt_token = get_token(request)
        except AuthenticationFailed:
            return None

        self.validate_token(jwt_token)
        payload = Token._decode(jwt_token)
        user = self.get_user(payload)
        return user, payload

    @staticmethod
    def validate_token(token) -> None:
        Token().check_token(token)

    def get_user(self, payload: dict) -> BaseAbstractUser:
        user_id = payload.get('user_id')
        user_role = payload.get('role')
        if not user_id:
            raise AuthenticationFailed('User identifier not found')
        if not user_role:
            raise AuthenticationFailed('User role not found')

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

        raise AuthenticationFailed('No such User role')
