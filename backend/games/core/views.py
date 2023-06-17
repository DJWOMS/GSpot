from rest_framework import viewsets, generics, status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django.shortcuts import get_object_or_404

from base import classes
from base.paginations import ProductResultsSetPagination
from core.models.product import GameDlcLink
from .filters import ProductFilter
from .serializers import (
    CreateProductSerializer,
    GameDlcLinkSerializer,
    ProductSerializer,
    SystemRequirementSerializer,
    GamesListSerializer,
    GameDetailSerializer,
    SaveToLibrarySerializer,
)
from .models import Product, SystemRequirement
from finance.models import Library, Offer, LibraryProduct


class ProductViewSet(classes.MixedPermissionSerializer, viewsets.ModelViewSet):
    pagination_class = ProductResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['name']
    filter_fields = ['price', 'name', 'platform', 'release_date', 'genres', 'subgenres']
    serializer_classes_by_action = {
        'create': CreateProductSerializer,
        'update': ProductSerializer,
        'destroy': ProductSerializer,
        'list': GamesListSerializer,
        'retrieve': GameDetailSerializer,
        'partial_update': ProductSerializer,
    }
    permission_classes_by_action = {
        'create': (IsAdminUser,),
        'update': (IsAdminUser,),
        'destroy': (IsAdminUser,),
        'list': (AllowAny,),
        'retrieve': (IsAuthenticated,),
        'partial_update': (IsAuthenticated,),
    }

    def get_queryset(self):
        return Product.objects.all()


class LinkDlcApiView(generics.CreateAPIView):
    serializer_class = GameDlcLinkSerializer


class SystemRequirementViewSet(classes.MixedPermissionSerializer, viewsets.ModelViewSet):
    serializer_classes_by_action = {
        'create': SystemRequirementSerializer,
        'update': SystemRequirementSerializer,
        'destroy': SystemRequirementSerializer,
        'list': SystemRequirementSerializer,
        'retrieve': SystemRequirementSerializer,
        'partial_update': SystemRequirementSerializer,
    }
    permission_classes_by_action = {
        'create': (IsAdminUser,),
        'update': (IsAdminUser,),
        'destroy': (IsAdminUser,),
        'list': (AllowAny,),
        'retrieve': (IsAuthenticated,),
        'partial_update': (IsAuthenticated,),
    }

    def get_queryset(self):
        return SystemRequirement.objects.all()


class SaveToLibraryAPIView(APIView):
    def post(self, request):
        serializer = SaveToLibrarySerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        user_to = request.query_params.get('user_to')
        offer_uuids = request.query_params.getlist('offer_uuid')

        if not user_to or not offer_uuids:
            return Response({'message': 'Missing required parameters.'}, status=400)

        library, _ = Library.objects.get_or_create(user=user_to)

        if library is None:
            return Response({'message': 'Failed to create library.'}, status=500)

        response = self.add_offers_to_library(library, offer_uuids)
        return response

    def add_offers_to_library(self, library, offer_uuids):
        for offer_uuid in offer_uuids:
            offer = get_object_or_404(Offer, id=offer_uuid)
            if offer is None:
                return Response(
                    {'message': f"Offer with ID {offer_uuid} does not exist or is not active."},
                    status=status.HTTP_404_NOT_FOUND
                )
            self.add_products_to_library(library, offer)

            return Response({'message': 'Games added to library successfully'}, status=200)

    def add_products_to_library(self, library, offer):
        products = offer.products.all()
        for product in products:
            library_product = LibraryProduct(library=library, product=product, offer=offer)
            library_product.save()
