from rest_framework import viewsets
from .models import Media, Reviews, RewiewAnswers
from .serializers import MediaSerializer, ReviewsSerializer, ReviewAnswersSerializer


class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer


class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer


class ReviewAnswersViewSet(viewsets.ModelViewSet):
    queryset = RewiewAnswers.objects.all()
    serializer_class = ReviewAnswersSerializer
