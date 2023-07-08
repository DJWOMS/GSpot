from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from core.models import Product
from finance.models import Library
from finance.serializers import OfferSerializer, LibrarySerializer, ProductContentShowSerializer


class OfferAPIView(APIView):
    def post(self, request):
        serializer = OfferSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ShowLibraryView(generics.RetrieveAPIView):
    serializer_class = LibrarySerializer
    queryset = Library.objects.all()
    lookup_field = 'user'


class ShowProductContentView(generics.RetrieveAPIView):
    serializer_class = ProductContentShowSerializer

    def get_queryset(self):
        return Product.objects.all()
