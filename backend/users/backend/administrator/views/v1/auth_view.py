from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView, Response
from administrator.serializers.v1.auth_serializer import AdminAuthSerializer
from base.serializers import AuthTokensResponseSerializer

from common.services.jwt.token import Token


class AdminAuthView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description='Получение администратором JWT токена',
        request_body=AdminAuthSerializer,
        responses={
            200: AuthTokensResponseSerializer,
            400: openapi.Response(description="Email or Password not valid"),
        },
        tags=["Авторизация", 'Администратор'],
    )
    def post(self, request):
        serializer = AdminAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        admin = serializer.validated_data["user"]
        data = {
            "user_id": str(admin.id),
            "role": admin._meta.app_label,
            "avatar": str(admin.avatar),
            "permissions": admin.permissions_codename,
        }

        tokens = Token().generate_tokens(data=data)

        response_serializer = AuthTokensResponseSerializer(data=tokens)
        response_serializer.is_valid(raise_exception=True)

        return Response(response_serializer.data, status=status.HTTP_200_OK)
