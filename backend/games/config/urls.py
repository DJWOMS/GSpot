from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/core', include('core.urls')),
    path('api/v1/reference/', include('reference.urls')),
]

# urls для swagger
urlpatterns += doc_urls
