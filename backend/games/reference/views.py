from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from .models import Language, ProductLanguage, Genre, SubGenre
from .serializers import (
    LanguageSerializer,
    ProductLanguageSerializer,
    GenreSerializer,
    SubGenreSerializer
)


class LanguageView(viewsets.ModelViewSet):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()


class ProductLangaugeView(viewsets.ModelViewSet):
    serializer_class = ProductLanguageSerializer
    queryset = ProductLanguage.objects.all()


class GenreView(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    permission_classes = (IsAdminUser,)

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return (AllowAny(),)
        else:
            return super().get_permissions()


class SubGenreView(viewsets.ModelViewSet):
    serializer_class = SubGenreSerializer
    queryset = SubGenre.objects.all()
