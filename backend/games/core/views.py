from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from base import classes
from .filters import ProductFilter
from .models import Product, SystemRequirement
from .serializers import (SystemRequirementSerializer,
                          ProductSerializer,
                          DlcSerializer,
                          ProductListSerializer)


class GameViewSet(classes.MixedPermissionSerializer, ModelViewSet):
    """ CRUD продукта """
    lookup_field = "name__iexact"
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    serializer_classes_by_action = {
        "create": ProductSerializer,
        "update": ProductSerializer,
        "destroy": ProductSerializer,
        "list": ProductListSerializer,
        "retrieve": ProductSerializer,
    }
    permission_classes_by_action = {
        "create": (IsAdminUser,),
        "update": (IsAdminUser,),
        "destroy": (IsAdminUser,),
        "list": (AllowAny,),
        "retrieve": (IsAuthenticated,)
    }

    def get_queryset(self):
        return Product.objects.filter(type=Product.TypeProduct.GAMES)




class DlcViewSet(classes.MixedPermissionSerializer, ModelViewSet):
    """ CRUD дополнений """
    serializer_classes_by_action = {
        "create": DlcSerializer,
        "update": DlcSerializer,
        "destroy": DlcSerializer,
        "list": DlcSerializer,
        "retrieve": DlcSerializer,
    }
    permission_classes_by_action = {
        "create": (IsAdminUser,),
        "update": (IsAdminUser,),
        "destroy": (IsAdminUser,),
        "list": (AllowAny,),
        "retrieve": (IsAuthenticated,),
    }

    def get_queryset(self):
        return Product.objects.filter(type=Product.TypeProduct.DLC)

class SystemRequirementViewSet(classes.MixedPermissionSerializer, ModelViewSet):
    """ CRUD дополнений """
    serializer_classes_by_action = {
        "create": SystemRequirementSerializer,
        "update": SystemRequirementSerializer,
        "destroy": SystemRequirementSerializer,
        "list": SystemRequirementSerializer,
        "retrieve": SystemRequirementSerializer,
    }
    permission_classes_by_action = {
        "create": (IsAdminUser,),
        "update": (IsAdminUser,),
        "destroy": (IsAdminUser,),
        "list": (AllowAny,),
        "retrieve": (IsAuthenticated,),
    }

    def get_queryset(self):
        return SystemRequirement.objects.all()
