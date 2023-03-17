from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Language, ProductLanguage, Genre, SubGenre
from .serializers import LanguageSerializer, ProductLanguageSerializer, GenreSerializer, SubGenreSerializer


class LanguageView(viewsets.ModelViewSet):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()


class ProductLangaugeView(viewsets.ModelViewSet):
    serializer_class = ProductLanguageSerializer
    queryset = ProductLanguage.objects.all()


class GenreView(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    get_permissions = (IsAdminUser,)
    lookup_field = 'name'

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrive':
            return (AllowAny(),)
        else:
            return super().get_permissions()


class SubGenreView(GenreView):
    queryset = SubGenre.objects.all()
    serializer_class = SubGenreSerializer
