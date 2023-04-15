from rest_framework import generics

from .models import Review
from .serializers import ReviewSerializer


class GameReviewCommentListView(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        game_uuid = self.kwargs['game_uuid']
        return Review.objects.filter(game__id=game_uuid)
