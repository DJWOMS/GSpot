from django.urls import path

from .views import GameReviewListView, GameReviewCommentListView, ReviewCreateView, CommentCreateView

urlpatterns = [
    path('review/<uuid:game_uuid>/', GameReviewListView.as_view(), name='review'),
    path('comments/<int:review_id>/', GameReviewCommentListView.as_view(), name='review-comments'),
    path('review/', ReviewCreateView.as_view(), name='add-review'),
    path('comment/', CommentCreateView.as_view(), name='add-comment'),
]
