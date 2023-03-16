from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Language, ProductLanguage, Group, GroupElement
from .serializers import LanguageSerializer, ProductLanguageSerializer, GroupSerializer, GroupElementSerializer


class LanguageView(viewsets.ModelViewSet):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()


class ProductLangaugeView(viewsets.ModelViewSet):
    serializer_class = ProductLanguageSerializer
    queryset = ProductLanguage.objects.all()


class GroupView(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    get_permissions = (IsAdminUser,)
    lookup_field = 'name'

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrive':
            return (AllowAny(),)
        else:
            return super().get_permissions()


class GroupElementView(GroupView):
    queryset = GroupElement.objects.all()
    serializer_class = GroupElementSerializer
