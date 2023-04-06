from rest_framework import viewsets

from django_filters.rest_framework import DjangoFilterBackend

from core.models import SystemRequirement
from core.serializers import OperatingSystemSerializer

from base.paginations import GamesResultsSetPagination

from finance.models.offer import Price

from reference.models.genres import Genre, SubGenre
from reference.serializers import GenreSerializer, SubGenreSerializer

from utils.serializers import MinMaxPriceSerializer


class GetOperatingSystemViewSet(viewsets.ReadOnlyModelViewSet):
    """List of operating systems"""

    serializer_class = OperatingSystemSerializer
    pagination_class = GamesResultsSetPagination
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        return [choice[1] for choice in SystemRequirement.OS.choices]


class GetGenreViewSet(viewsets.ReadOnlyModelViewSet):
    """List of genres"""

    serializer_class = GenreSerializer
    pagination_class = GamesResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    queryset = Genre.objects.all()


class GetSubGenreViewSet(viewsets.ReadOnlyModelViewSet):
    """List of all sub-genres"""

    serializer_class = SubGenreSerializer
    pagination_class = GamesResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    queryset = SubGenre.objects.all()


class GetMinMaxPriceViewSet(viewsets.ReadOnlyModelViewSet):
    """Min and Max price of product"""

    serializer_class = MinMaxPriceSerializer
    pagination_class = GamesResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    queryset = Price.objects.all()
