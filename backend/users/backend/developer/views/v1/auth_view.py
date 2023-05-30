from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView, Response
from base.serializers import AuthTokensResponseSerializer
from developer.serializers.v1.auth_serializer import DeveloperAuthSerializer

from common.services.jwt.token import Token


class DeveloperAuthView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description='Получение разработчиком JWT токена',
        request_body=DeveloperAuthSerializer,
        responses={
            200: AuthTokensResponseSerializer,
            400: openapi.Response(description="Email or Password not valid"),
        },
        tags=["Аутентификация", "Разработчик"],
    )
    def post(self, request):
        serializer = DeveloperAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        developer = serializer.validated_data["user"]
        data = {
            "user_id": str(developer.id),
            "role": developer._meta.app_label,
            "avatar": str(developer.avatar),
            "permissions": developer.permissions_codename,
        }

        tokens = Token().generate_tokens(data=data)

        response_serializer = AuthTokensResponseSerializer(data=tokens)
        response_serializer.is_valid(raise_exception=True)

        return Response(response_serializer.data, status=status.HTTP_200_OK)
