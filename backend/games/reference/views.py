from rest_framework import viewsets
from .models import Language, ProductLanguage
from .serializers import LanguageSerializer, ProductLanguageSerializer


class LanguageView(viewsets.ModelViewSet):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()


class ProductLangaugeView(viewsets.ModelViewSet):
    serializer_class = ProductLanguageSerializer
    queryset = ProductLanguage.objects.all()
