from django.contrib import admin
from django.urls import path

from .yasg import urlpatterns as yasg_doc
from common.urls import urlpatterns as common_urls

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += yasg_doc
urlpatterns += common_urls
