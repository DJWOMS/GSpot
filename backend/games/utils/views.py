from rest_framework import generics
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from core.models import SystemRequirement
from core.serializers import OperatingSystemSerializer

from reference.models.genres import Genre, SubGenre
from reference.serializers import GenreGamesSerializer

from .serializers import MinMaxPriceSerializer


class GetOperatingSystemListView(generics.ListAPIView):
    """List of operating systems"""

    serializer_class = OperatingSystemSerializer
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        return SystemRequirement.objects.values_list('operating_system', flat=True).distinct()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        os_names = dict(SystemRequirement.OSChoices.choices)
        platforms = [os_names[os] for os in queryset]
        return Response(platforms)


class GetGenreListView(generics.ListAPIView):
    """List of genres"""

    serializer_class = GenreGamesSerializer
    filter_backends = [DjangoFilterBackend]
    queryset = Genre.objects.prefetch_related('subgenres')

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()

        queryset = kwargs.get('queryset') or self.filter_queryset(self.get_queryset())

        subgenres = SubGenre.objects.filter(genre__in=queryset).order_by('genre_id', 'name')

        kwargs['context'] = self.get_serializer_context()
        kwargs['context']['subgenres'] = subgenres

        return serializer_class(*args, **kwargs)

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)

        subgenre_ids = self.request.query_params.getlist('subgenre')
        if subgenre_ids:
            queryset = queryset.filter(subgenres__id__in=subgenre_ids).distinct()

        return queryset


class GetMinMaxPriceListView(generics.GenericAPIView):
    """Returns the minimum and maximum price for a product"""

    serializer_class = MinMaxPriceSerializer
    filter_backends = [DjangoFilterBackend]

    def get_serializer(self, *args, **kwargs):
        return MinMaxPriceSerializer(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data={})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
