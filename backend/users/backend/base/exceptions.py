from rest_framework.exceptions import APIException


class AuthenticationFailed(APIException):
    status_code = 401
