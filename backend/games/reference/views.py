from rest_framework import viewsets
from . import models
from . import serializers


class LanguageView(viewsets.ModelViewSet):
    serializer_class = serializers.LanguageSerializer
    queryset = models.Language.objects.all()


class ProductLangaugeView(viewsets.ModelViewSet):
    serializer_class = serializers.ProductLanguageSerializer
    queryset = models.ProductLanguage.objects.all()
