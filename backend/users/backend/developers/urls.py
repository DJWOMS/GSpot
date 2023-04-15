from django.urls import path, include
from rest_framework import routers

from . import views
from .views import CompanyUserViewSet

router = routers.DefaultRouter()
router.register(r'company_employee', views.CompanyEmployeeViewSet, basename='company_employee')
router.register(r'users', CompanyUserViewSet)

urlpatterns = [
    path('company/<int:pk>/', views.CompanyRetrieveUpdateDeleteView.as_view(), name='company_detail'),
    path('company/<int:pk>/employees/', views.CompanyEmployeeListView.as_view(), name='company_employee_list'),
    path('admin/companies/', views.CompanyAdminListView.as_view(), name='company_admin_list'),
    path('admin/company/<int:pk>/', views.CompanyAdminDetailView.as_view(), name='company_admin_detail'),
    path('', include(router.urls)),
]
