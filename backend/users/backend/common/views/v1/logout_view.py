from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from common.serializers.v1.logout_serializer import LogoutSerializer
from common.services.jwt.blacklist import TokenBlackList


@method_decorator(
    name='post',
    decorator=swagger_auto_schema(
        operation_description='Прекратить сеанс работы в качестве зарегистрированного пользователя',
        tags=[
            'Аутентификация',
        ],
        request_body=LogoutSerializer,
        responses={
            200: openapi.Response(
                'Сеанс работы прекращен',
            ),
            400: openapi.Response('Отсутствует refresh токен'),
        },
    ),
)
class JWTLogoutView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = LogoutSerializer

    def post(self, request):
        try:
            token = request.data.get('refresh_token')
            blacklist = TokenBlackList(token)
            blacklist.add()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
