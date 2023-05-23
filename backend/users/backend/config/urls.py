from django.contrib import admin
from django.urls import path, include

from .yasg import urlpatterns as yasg_doc
from developer.urls import urlpatterns as develop_url
from administrator.urls import urlpatterns as admin_url
from customer.urls import urlpatterns as customer_url

v1 = [
    path('admin/', include('administrator.urls')),
    path('developer/', include('developer.urls')),
    path('customer/', include('customer.urls')),
]

urlpatterns = [
    path('api/v1/', include(v1)),
    path('admin/', admin.site.urls),
    path('api/users/', include('common.urls')),
]

urlpatterns += yasg_doc
urlpatterns += admin_url
urlpatterns += develop_url
urlpatterns += customer_url
