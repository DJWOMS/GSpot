from django_filters import rest_framework as filters
from .models import Product


class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name='offers__price__amount', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='offers__price__amount', lookup_expr='lte')
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    platform = filters.CharFilter(field_name='system_requirements__operating_system',
                                  lookup_expr='icontains')
    created_after = filters.DateFilter(field_name='release_date', lookup_expr='gte')
    created_before = filters.DateFilter(field_name='release_date', lookup_expr='lte')
    genres = filters.CharFilter(field_name='genres__name', lookup_expr='icontains')
    subgenres = filters.CharFilter(field_name='subgenres__name', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = (
            'min_price', 'max_price', 'name',
            'platform', 'created_after', 'created_before',
            'genres', 'subgenres'
        )


# class DlcFilter(filters.FilterSet):
#     name = filters.CharFilter(field_name='name', lookup_expr='icontains')
#
#     class Meta:
#         model = models.GameDlcLink
#         fields = ('name')
