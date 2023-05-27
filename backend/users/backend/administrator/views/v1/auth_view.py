from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView, Response
from administrator.serializers.v1.auth_serializer import AdminAuthSerializer

from common.services.jwt.token import Token


class AdminAuthView(APIView):
    permission_classes = [AllowAny]

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

        return Response(tokens, status=status.HTTP_200_OK)
