from django.urls import path, include
from rest_framework import routers
from .views import MediaViewSet, ReviewsViewSet, ReviewAnswersViewSet

router = routers.DefaultRouter()
router.register(r'media', MediaViewSet)
router.register(r'reviews', ReviewsViewSet)
router.register(r'review_answers', ReviewAnswersViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
