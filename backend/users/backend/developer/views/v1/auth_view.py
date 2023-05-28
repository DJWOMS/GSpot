from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView, Response
from developer.serializers.v1.auth_serializer import DeveloperAuthSerializer

from common.services.jwt.token import Token


class DeveloperAuthView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "email": openapi.Schema(type=openapi.TYPE_STRING),
                "password": openapi.Schema(type=openapi.TYPE_STRING),
            },
            required=["email", "password"],
        ),
        responses={
            200: openapi.Response(
                description="Successful authentication",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "tokens": openapi.Schema(type=openapi.TYPE_STRING),
                    },
                ),
            ),
            400: openapi.Response(description="Email or Password not valid"),
        },
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

        return Response(tokens, status=status.HTTP_200_OK)
