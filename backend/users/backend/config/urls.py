from django.contrib import admin
from django.urls import path

from administrator.views.v1.employee_crud import EmployeeListView, EmployeeDetailView
from .yasg import urlpatterns as yasg_doc

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/administrator/admin/employee/', EmployeeListView.as_view()),
    path('api/v1/administrator/admin/employee/<uuid:pk>/', EmployeeDetailView.as_view()),
]

urlpatterns += yasg_doc
