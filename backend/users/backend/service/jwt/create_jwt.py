from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken

from service.jwt.get_permissions import get_dict_of_user_permissions


def get_token_user(user, role):
    data = {}
    token = RefreshToken.for_user(user)
    token['user_id'] = str(user.id)
    token['role'] = role
    token['permissions'] = get_dict_of_user_permissions(user)
    data['refresh'] = str(token)
    data['access'] = str(token.access_token)
    if api_settings.UPDATE_LAST_LOGIN:
        update_last_login(None, user)
    return data