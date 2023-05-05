from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as yasg_doc

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/admin/', include('administrator.urls')),
    path('api/v1/customer/', include('customer.urls')),
    path('api/v1/company/', include('developer.urls')),
]

urlpatterns += yasg_doc
