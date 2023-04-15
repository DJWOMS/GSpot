from django.urls import path

from .views import GameReviewListView, GameReviewCommentListView

urlpatterns = [
    path('review/<uuid:game_uuid>/', GameReviewListView.as_view(), name='review'),
    path('review/comments/<int:review_id>/', GameReviewCommentListView.as_view(), name='review-comments')
]
