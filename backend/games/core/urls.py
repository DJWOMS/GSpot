from django.urls import path

from core import views

urlpatterns = [
    path('products/', views.ProductView.as_view({
        "get": "list", "post": "create"
    }), name="products"),
    path('products/<str:name__iexact>/', views.ProductView.as_view({
        "get": "retrieve", "delete": "retrieve", "patch": "update"
    }), name="product"),

    path('dlc/', views.DlcView.as_view({
        "get": "list", "post": "create"
    }), name="dlc-all"),
    path('dlc/<int:pk>/', views.DlcView.as_view({
        "get": "retrieve", "delete": "retrieve", "patch": "update"
    }), name="dlc")
]
