from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from base.paginations import CommentsResultsSetPagination

from .models import Comment, Reaction, Review
from .serializers import ReviewSerializer, CommentSerializer, ReactionSerializer


class GameReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        game_uuid = self.kwargs['game_uuid']
        return Review.objects.filter(game__id=game_uuid)


class GameReviewCommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer
    pagination_class = CommentsResultsSetPagination

    def get_queryset(self):
        review_id = self.kwargs['review_id']
        return Comment.objects.filter(review__id=review_id)


class ReactionCreateView(generics.CreateAPIView):
    serializer_class = ReactionSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = ReactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        reaction = Reaction.objects.filter(user_uuid=serializer.data['user_uuid']).first()

        if not reaction:
            return super().post(request, *args, **kwargs)

        if reaction.like_type == serializer.data['like_type']:
            reaction.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            reaction.like_type = serializer.data['like_type']
            reaction.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
