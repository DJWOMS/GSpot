from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView, Response
from developer.serializers.v1.auth_serializer import DeveloperAuthSerializer

from common.services.jwt.token import Token


class DeveloperAuthView(APIView):
    permission_classes = [AllowAny]

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
