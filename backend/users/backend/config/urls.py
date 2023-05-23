from django.urls import path, include

from .yasg import urlpatterns as yasg_doc

v1 = [
    path('admin/', include('administrator.urls')),
    path('developer/', include('developer.urls')),
    path('customer/', include('customer.urls')),
]

urlpatterns = [
    path('api/v1/', include(v1)),
    path('api/users/', include('common.urls')),
]

urlpatterns += yasg_doc
