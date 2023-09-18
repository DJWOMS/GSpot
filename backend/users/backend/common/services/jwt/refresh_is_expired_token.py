from common.services.jwt.token import Token
from django.conf import settings


def get_expired_time_token(refresh_token):
    exp_left = Token().check_exp_left(refresh_token)
    return exp_left > int(settings.REFRESH_TOKEN_ROTATE_MIN_LIFETIME.total_seconds())


def update_access_token(refresh_token, user):
    if get_expired_time_token(refresh_token):
        dict_token = {
            'refresh': refresh_token,
            'access': Token().generate_access_token_for_user(user),
        }
    else:
        dict_token = Token().generate_tokens_for_user(user)
    return dict_token
