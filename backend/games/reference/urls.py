from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import LanguageView, ProductLangaugeView, GenreView, SubGenreView

api_router = DefaultRouter()
api_router.register('languages', LanguageView, basename='languages')
api_router.register('product_languages', ProductLangaugeView, basename='product_languages')
api_router.register('genre', GenreView, basename='genre')
api_router.register('subgenre', SubGenreView, basename='subgenre')

urlpatterns = [
    path('', include(api_router.urls))
]
