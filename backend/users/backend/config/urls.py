from django.contrib import admin
from django.urls import path, include


from .yasg import urlpatterns as yasg_doc
from common.services.jwt.urls import urlpatterns as jwt_url



urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += yasg_doc
urlpatterns += jwt_url
