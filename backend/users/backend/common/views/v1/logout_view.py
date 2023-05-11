from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from common.services.jwt.blacklist import TokenBlackList
from common.services.jwt.request import get_token


class JWTLogoutView(APIView):
    def post(self, request):
        try:
            token = get_token(request)
            blacklist = TokenBlackList(token)
            blacklist.add()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
