from django_filters import rest_framework as filters
from . import models


class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = models.Product
        fields = ('name', 'status', 'type')


# class DlcFilter(filters.FilterSet):
#     name = filters.CharFilter(field_name='name', lookup_expr='icontains')
#
#     class Meta:
#         model = models.GameDlcLink
#         fields = ('name')
