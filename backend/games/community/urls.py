from django.urls import path

from .views import GameReviewCommentListView

urlpatterns = [
    path('review/<uuid:game_uuid>/', GameReviewCommentListView.as_view(), name='review'),
]
