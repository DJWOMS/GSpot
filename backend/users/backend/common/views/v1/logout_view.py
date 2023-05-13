from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from common.services.jwt.blacklist import TokenBlackList


class JWTLogoutView(GenericAPIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            token = request.data.get('refresh_token')
            blacklist = TokenBlackList(token)
            blacklist.add()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
