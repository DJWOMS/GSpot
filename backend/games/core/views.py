from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from base import classes
from . import filters
from . import serializers, models

class GameViewSet(classes.MixedPermissionSerializer, viewsets.ModelViewSet):
    """ CRUD продукта """
    # lookup_field = 'id'
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.ProductFilter
    serializer_classes_by_action = {
        'create': serializers.ProductSerializer,
        'update': serializers.ProductSerializer,
        'destroy': serializers.ProductSerializer,
        'list': serializers.ProductSerializer,
        'retrieve': serializers.ProductSerializer,
        'partial_update':serializers.ProductSerializer,
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
        return models.Product.objects.filter(type=models.Product.TypeProduct.GAMES)




class DlcViewSet(classes.MixedPermissionSerializer, viewsets.ModelViewSet):
    """ CRUD дополнений """
    serializer_classes_by_action = {
        'create': serializers.DlcSerializer,
        'update': serializers.DlcSerializer,
        'destroy': serializers.DlcSerializer,
        'list': serializers.DlcSerializer,
        'retrieve': serializers.DlcSerializer,
    }
    permission_classes_by_action = {
        'create': (IsAdminUser,),
        'update': (IsAdminUser,),
        'destroy': (IsAdminUser,),
        'list': (AllowAny,),
        'retrieve': (IsAuthenticated,),
    }

    def get_queryset(self):
        return models.Product.objects.filter(type=models.Product.TypeProduct.DLC)

class SystemRequirementViewSet(classes.MixedPermissionSerializer, viewsets.ModelViewSet):
    """ CRUD системных требований """
    serializer_classes_by_action = {
        'create': serializers.SystemRequirementSerializer,
        'update': serializers.SystemRequirementSerializer,
        'destroy': serializers.SystemRequirementSerializer,
        'list': serializers.SystemRequirementSerializer,
        'retrieve': serializers.SystemRequirementSerializer,
    }
    permission_classes_by_action = {
        'create': (IsAdminUser,),
        'update': (IsAdminUser,),
        'destroy': (IsAdminUser,),
        'list': (AllowAny,),
        'retrieve': (IsAuthenticated,),
    }
    def get_queryset(self):
        return models.SystemRequirement.objects.all()

class GameDlcLinkViewSet(classes.MixedPermissionSerializer, viewsets.ModelViewSet):
    """ CRUD связки игры с дополнением """
    serializer_classes_by_action = {
        'create': serializers.GameDlcLinkSerializer,
        'update': serializers.GameDlcLinkSerializer,
        'destroy': serializers.GameDlcLinkSerializer,
        'list': serializers.GameDlcLinkSerializer,
        'retrieve': serializers.GameDlcLinkSerializer,
    }
    permission_classes_by_action = {
        'create': (IsAdminUser,),
        'update': (IsAdminUser,),
        'destroy': (IsAdminUser,),
        'list': (AllowAny,),
        'retrieve': (IsAuthenticated,),
    }

    def get_queryset(self):
        return models.GameDlcLink.objects.all()
