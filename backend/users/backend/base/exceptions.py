from rest_framework import status
from rest_framework.exceptions import APIException


class AuthenticationFailed(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED


class UserInActive(Exception):
    pass


class UserBanned(Exception):
    pass
