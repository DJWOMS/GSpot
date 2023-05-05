from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from base import classes
from base.paginations import GamesResultsSetPagination
from .filters import ProductFilter
from .serializers import (
    CreateProductSerializer,
    ProductSerializer,
    SystemRequirementSerializer,
    GamesListSerializer,
    GameDetailSerializer
)
from .models import Product, SystemRequirement


class ProductViewSet(classes.MixedPermissionSerializer, viewsets.ModelViewSet):
    pagination_class = GamesResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    serializer_classes_by_action = {
        'create': CreateProductSerializer,
        'update': ProductSerializer,
        'destroy': ProductSerializer,
        'list': GamesListSerializer,
        'retrieve': GameDetailSerializer,
        'partial_update': ProductSerializer,
    }
    permission_classes_by_action = {
        'create': (AllowAny,),
        'update': (IsAdminUser,),
        'destroy': (IsAdminUser,),
        'list': (AllowAny,),
        'retrieve': (IsAuthenticated,),
        'partial_update': (IsAuthenticated,),
    }

    def get_queryset(self):
        return Product.objects.all()


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
