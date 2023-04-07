from rest_framework import generics
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from core.models import SystemRequirement
from core.serializers import OperatingSystemSerializer

from base.paginations import GamesResultsSetPagination

from reference.models.genres import Genre, SubGenre
from reference.serializers import GenreSerializer

from .serializers import MinMaxPriceSerializer, SubGenreByGenreIdSerializer


class GetOperatingSystemListView(generics.ListAPIView):
    """List of operating systems"""

    serializer_class = OperatingSystemSerializer
    pagination_class = GamesResultsSetPagination
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        return SystemRequirement.objects.values('operating_system').distinct()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        platforms = [req['operating_system'] for req in queryset]
        return Response(platforms)


class GetGenreListView(generics.ListAPIView):
    """List of genres"""

    serializer_class = GenreSerializer
    pagination_class = GamesResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    queryset = Genre.objects.all()


class GetSubGenreListView(generics.ListAPIView):
    """List of all sub-genres"""

    serializer_class = SubGenreByGenreIdSerializer
    pagination_class = GamesResultsSetPagination
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        genre_id = self.kwargs['genre_id']
        return SubGenre.objects.filter(genre_id=genre_id)


class GetMinMaxPriceListView(generics.GenericAPIView):
    """Returns the minimum and maximum price for a product"""

    serializer_class = MinMaxPriceSerializer
    pagination_class = GamesResultsSetPagination
    filter_backends = [DjangoFilterBackend]

    def get_serializer(self, *args, **kwargs):
        return MinMaxPriceSerializer(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer()
        return Response(serializer.data)
