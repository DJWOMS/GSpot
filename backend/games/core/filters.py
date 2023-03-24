from django_filters import rest_framework as filters
from .models import Product


class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ('name', 'status', 'type')


# class DlcFilter(filters.FilterSet):
#     name = filters.CharFilter(field_name='name', lookup_expr='icontains')
#
#     class Meta:
#         model = models.GameDlcLink
#         fields = ('name')
