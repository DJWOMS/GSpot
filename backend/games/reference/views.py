from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
<<<<<<< HEAD
from .models import Language, ProductLanguage, Group, GroupElement
from .serializers import LanguageSerializer, ProductLanguageSerializer, GroupSerializer, GroupElementSerializer


class LanguageView(viewsets.ModelViewSet):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()


class ProductLangaugeView(viewsets.ModelViewSet):
    serializer_class = ProductLanguageSerializer
    queryset = ProductLanguage.objects.all()
=======
from games.reference.serializers import GenreSerializer, SubGenreSerializer
from models import Genre, SubGenre
>>>>>>> 2c402bf (исправлены модели и названия классов в соответсвии с моделями   файлах в views,admin,serializers)


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
