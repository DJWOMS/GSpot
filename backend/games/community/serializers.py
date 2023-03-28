from rest_framework import serializers
from .models import Media, Social, Review, ReviewAnswer


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        exclude = ('product',)


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('game', 'text', 'grade')


class ReviewAnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewAnswer
        fields = ('review', 'text', 'grade')
