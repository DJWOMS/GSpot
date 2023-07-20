from django.urls import path

from .views import GameReviewListView, GameReviewCommentListView, ReactionCreateView

urlpatterns = [
    path('reaction/', ReactionCreateView.as_view(), name='reaction'),
    path('review/<uuid:game_uuid>/', GameReviewListView.as_view(), name='review'),
    path('comments/<int:review_id>/', GameReviewCommentListView.as_view(), name='review-comments')
]
