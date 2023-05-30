from django.urls import path, include

from .yasg import urlpatterns as yasg_doc

v1 = [
    path('admin/', include('administrator.urls')),
    path('developer/', include('developer.urls')),
    path('customer/', include('customer.urls')),
    path('common/', include('common.urls')),
]

urlpatterns = [
    path('api/v1/', include(v1)),
]

urlpatterns += yasg_doc
