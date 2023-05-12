from django.contrib import admin
from django.urls import path

from .yasg import urlpatterns as yasg_doc
from developer.urls import urlpatterns as develop_url
from administrator.urls import urlpatterns as admin_url
from customer.urls import urlpatterns as customer_url


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += yasg_doc
urlpatterns += admin_url
urlpatterns += develop_url
urlpatterns += customer_url
