from common.services.jwt.token import Token
from django.conf import settings


def get_expired_time_token(refresh_token):
    exp_left = Token().check_exp_left(refresh_token)
    return exp_left > int(settings.REFRESH_TOKEN_ROTATE_MIN_LIFETIME.total_seconds())
