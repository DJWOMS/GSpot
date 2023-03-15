from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from . import models, serializers


class LanguageView(viewsets.ModelViewSet):
    serializer_class = serializers.LanguageSerializer
    queryset = models.Language.objects.all()


class ProductLangaugeView(viewsets.ModelViewSet):
    serializer_class = serializers.ProductLanguageSerializer
    queryset = models.ProductLanguage.objects.all()


class GroupView(viewsets.ModelViewSet):
    queryset = models.Group.objects.all()
    serializer_class = serializers.GroupSerializer
    get_permissions = (IsAdminUser,)
    lookup_field = 'name'

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrive':
            return (AllowAny(),)
        else:
            return super().get_permissions()


class GroupElementView(GroupView):
    queryset = models.GroupElement.objects.all()
    serializer_class = serializers.GroupElementSerializer

