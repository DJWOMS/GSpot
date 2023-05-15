from rest_framework import viewsets, generics, status, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

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
    GameDetailSerializer
)
from .models import Product, SystemRequirement


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
