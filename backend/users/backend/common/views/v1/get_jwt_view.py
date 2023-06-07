from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from common.serializers.v1.get_jwt_serializers import GetJwtSerializers, ResponseGetJwtSerializers
from rest_framework.response import Response
from common.services.jwt.token import Token


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
        data = request.data
        context = self.get_serializer_context()
        token = Token()
        serializer = GetJwtSerializers(data=data, context=context)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        if serializer.validated_data['exp_left']:
            dict_token = {
                'refresh': data.get('refresh_token'),
                'access': token.generate_access_token_for_user(user),
            }
        else:
            dict_token = token.generate_tokens_for_user(user)
        dict_token = ResponseGetJwtSerializers(data=dict_token)
        dict_token.is_valid(raise_exception=True)
        return Response(dict_token.data, status=status.HTTP_200_OK)
