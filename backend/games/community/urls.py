from django.urls import path, include
from rest_framework import routers
from .views import MediaViewSet, ReviewViewSet

router = routers.DefaultRouter()
router.register(r'media', MediaViewSet)
router.register(r'reviews', ReviewViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
