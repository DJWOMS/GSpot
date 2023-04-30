from django.contrib import admin
from django.urls import path

from .yasg import urlpatterns as yasg_doc


urlpatterns = [
    path('admin/', admin.site.urls),
	
]

urlpatterns += yasg_doc
