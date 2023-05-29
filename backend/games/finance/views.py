from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from finance.models import Offer, Library
from core.serializers import GamesListSerializer
from drf_yasg import openapi

from finance.serializers import (
    OfferSerializer, LibrarySerializer, OfferInCartSerializerCreate
)


class OfferAPIView(APIView):

    @swagger_auto_schema(
        operation_description="description",
        responses={200: openapi.Response('Создание пакета игр или одной игры', OfferSerializer())},
        request_body=OfferSerializer
    )
    def post(self, request):
        serializer = OfferSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ShowLibraryView(generics.RetrieveAPIView):
    serializer_class = LibrarySerializer
    queryset = Library.objects.all()
    lookup_field = 'user'


class OfferInCartAPIView(APIView):
    @swagger_auto_schema(
        operation_description="description",
        responses={200: openapi.Response('Добавление в корзину', OfferInCartSerializerCreate())},
        request_body=OfferInCartSerializerCreate)
    def post(self, request):
        offer = get_object_or_404(Offer, id=request.data.get('offers'))
        offer_serializer = OfferInCartSerializerCreate(data=request.data)
        offer_serializer.is_valid(raise_exception=True)
        offer_serializer.save()
        games = offer.products.all()
        game_serializer = GamesListSerializer(games, many=True)
        return Response(game_serializer.data)
