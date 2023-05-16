from rest_framework.response import Response
from rest_framework.views import APIView

from finance.serializers import OfferSerializer


class OfferAPIView(APIView):
    def post(self, request):
        serializer = OfferSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
