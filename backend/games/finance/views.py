from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView
from finance.models import Offer
from rest_framework.exceptions import ValidationError
from core.serializers import GamesListSerializer
from drf_yasg import openapi
from rest_framework import generics
from finance.models import Library
from finance.serializers import (
    OfferSerializer, LibrarySerializer, CartSerializerCreate
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


class CartAPIView(APIView):
    @swagger_auto_schema(
        operation_description="description",
        responses={200: openapi.Response('Добавление в корзину', CartSerializerCreate())},
        request_body=CartSerializerCreate)
    def post(self, request):
        offer = Offer.objects.get(id=request.data.get('offers')[0])
        if offer.cart.filter(created_by=request.data.get('created_by')).exists():
            raise ValidationError('Эта игра или сборник игр уже в корзине у пользователя.')
        offer_serializer = CartSerializerCreate(data=request.data)
        offer_serializer.is_valid(raise_exception=True)
        offer_serializer.save()
        games = offer.products.all()
        game_serializer = GamesListSerializer(games, many=True)
        return Response(game_serializer.data)


class ShowLibraryView(generics.RetrieveAPIView):
    serializer_class = LibrarySerializer
    queryset = Library.objects.all()
    lookup_field = 'user'
