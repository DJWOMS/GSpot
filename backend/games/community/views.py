from rest_framework import generics

from .models import Comment, Review
from .serializers import ReviewSerializer, CommentSerializer


class GameReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        game_uuid = self.kwargs['game_uuid']
        return Review.objects.filter(game__id=game_uuid)


class GameReviewCommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        review_id = self.kwargs['review_id']
        return Comment.objects.filter(review__id=review_id)