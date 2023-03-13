from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from base import classes
from . import serializers, models
from .filters import ProductFilter


class ProductView(classes.MixedPermissionSerializer, ModelViewSet):
    """ CRUD продукта """
    lookup_field = "name__iexact"
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    serializer_classes_by_action = {
        "create": serializers.ProductSerializer,
        "update": serializers.ProductSerializer,
        "destroy": serializers.ProductSerializer,
        "list": serializers.ProductListSerializer,
        "retrieve": serializers.ProductSerializer,
    }
    permission_classes_by_action = {
        "create": (IsAdminUser,),
        "update": (IsAdminUser,),
        "destroy": (IsAdminUser,),
        "list": (AllowAny,),
        "retrieve": (IsAuthenticated,)
    }

    def get_queryset(self):
        return models.Product.objects.all()


class DlcView(classes.MixedPermissionSerializer, ModelViewSet):
    """ CRUD дополнений """
    serializer_classes_by_action = {
        "create": serializers.DlcSerializer,
        "update": serializers.DlcSerializer,
        "destroy": serializers.DlcSerializer,
        "list": serializers.DlcSerializer,
        "retrieve": serializers.DlcSerializer,
    }
    permission_classes_by_action = {
        "create": (IsAdminUser,),
        "update": (IsAdminUser,),
        "destroy": (IsAdminUser,),
        "list": (AllowAny,),
        "retrieve": (IsAuthenticated,),
    }

    def get_queryset(self):
        return models.GameDlcLink.objects.all()
