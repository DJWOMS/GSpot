from django.contrib import admin
from django.urls import path, include


from .yasg import urlpatterns as yasg_doc
from service.jwt.urls_jwt import urlpatterns as jwt_url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
]
urlpatterns += yasg_doc
urlpatterns += jwt_url
