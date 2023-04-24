from django.urls import path, include
from rest_framework import routers

from developer.views.v1.views import CompanyUserViewSet, CompanyViewSet

router = routers.DefaultRouter()
router.register(r'users', CompanyUserViewSet, basename='company_users')
router.register(r'companies', CompanyViewSet, basename='company')

urlpatterns = [
    path('', include(router.urls)),
]
