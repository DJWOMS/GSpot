from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from common.serializers.v1.get_jwt_serializers import GetJwtSerializers, ResponseGetJwtSerializers
from rest_framework.response import Response
from common.services.jwt.token import Token

from common.services.jwt.expired_time_token import get_expired_time_token


@method_decorator(
    name='post',
    decorator=swagger_auto_schema(
        request_body=GetJwtSerializers,
        operation_description='Обновление refresh токена - или получения access токена',
        tags=['Аутентификация', 'Администратор', 'Разработчик', 'Пользователь'],
        responses={
            200: openapi.Response('Токен успешно обновлен'),
            401: openapi.Response('Ошибка обновления токена'),
        },
    ),
)
class GetJwtView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    http_method_names = ['post']

    def post(self, request):
        token = Token()
        serializer = GetJwtSerializers(data=request.data, context=self.get_serializer_context())
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh_token = serializer.validated_data['refresh_token']
        if get_expired_time_token(refresh_token):
            dict_token = {
                'refresh': refresh_token,
                'access': token.generate_access_token_for_user(user),
            }
        else:
            dict_token = token.generate_tokens_for_user(user)
        return Response(dict_token, status=status.HTTP_200_OK)
