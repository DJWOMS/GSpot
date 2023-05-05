from django.contrib import admin
from django.urls import path

from administrator.views.v1.employee_crud import (
    EmployeeListView,
    EmployeeDetailView,
    EmployeePermissionsView,
)

urlpatterns = [
    path('employee/', EmployeeListView.as_view()),
    path('employee/<uuid:pk>/', EmployeeDetailView.as_view()),
    path('employee/<uuid:pk>/permissions/', EmployeePermissionsView.as_view()),
]
