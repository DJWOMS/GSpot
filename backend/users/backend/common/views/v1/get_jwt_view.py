from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from common.serializers.v1.get_jwt_serializers import GetJwtSerializers
from rest_framework.response import Response


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
        serializer = GetJwtSerializers(data=data, context=context)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data
        return Response(token, status=status.HTTP_200_OK)
