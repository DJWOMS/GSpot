from django.contrib import admin
from django.urls import path

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('products/', views.ProductView.as_view({
        "get": "list", "post": "create"
    }), name="products"),
    path('products/<str:name__iexact>/', views.ProductView.as_view({
        "get": "retrieve", "delete": "retrieve", "patch": "update"
    }), name="product")
]
