from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import LanguageView, ProductLangaugeView

api_router = DefaultRouter()
api_router.register('languages', LanguageView, basename='languages')
api_router.register('product_languages', ProductLangaugeView, basename='product_languages')

urlpatterns = [
    path('', include(api_router.urls))
]
