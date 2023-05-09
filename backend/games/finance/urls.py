from django.urls import path

from views import GetProductsLibraryRetrieve


urlpatterns = [
    path("finance/library/<user>", GetProductsLibraryRetrieve.as_view(),
         name="all_products_in_library")
]
