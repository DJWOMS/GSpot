from django.urls import path, include
from rest_framework import routers
from .views import MediaViewSet

router = routers.DefaultRouter()
router.register('media', MediaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
