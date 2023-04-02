from rest_framework import serializers
from .models import Media, Social, Review, Comment, Reaction


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


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('text',)


class LikeDislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = ('like_type',)
