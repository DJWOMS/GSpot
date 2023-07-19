from django.urls import path

from .views import GameReviewListView, GameReviewCommentListView, ReviewCreateAPIView

urlpatterns = [
    path('add_review/', ReviewCreateAPIView.as_view(), name='add-review'),
    path('review/<uuid:game_uuid>/', GameReviewListView.as_view(), name='review'),
    path('comments/<int:review_id>/', GameReviewCommentListView.as_view(), name='review-comments'),
]
