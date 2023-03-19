from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

api_router = DefaultRouter()
api_router.register('languages', views.LanguageView, basename='languages')
api_router.register('product_languages', views.ProductLangaugeView, basename='product_languages')

urlpatterns = [
    path('', include(api_router.urls))
]
