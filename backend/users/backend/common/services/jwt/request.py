from django.conf import settings
from base.exceptions import AuthenticationFailed


def get_token(request) -> str:
    if settings.GET_TOKEN_FROM == 'header':
        token = get_token_from_header(request)
    else:
        token = get_token_from_cookies(request)

    if not token:
        raise AuthenticationFailed('Token not found in %s' % settings.GET_TOKEN_FROM)
    return token


def get_token_from_header(request) -> str:
    token = request.META.get('HTTP_AUTHORIZATION')
    return token


def get_token_from_cookies(request) -> str:
    token = request.COOKIES.get('Authentication')
    return token
