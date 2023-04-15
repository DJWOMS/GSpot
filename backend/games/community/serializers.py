from django.db.models import Count

from rest_framework import serializers

from .models import Media, Social, Review, Comment, Reaction


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = ['id', 'like_type']


class ReviewSerializer(serializers.ModelSerializer):
    reactions = serializers.SerializerMethodField()
    language = serializers.StringRelatedField()

    class Meta:
        model = Review
        fields = '__all__'

    def get_reactions(self, obj):
        reactions = Reaction.objects.filter(review=obj)
        likes = reactions.filter(like_type='Like').count()
        dislikes = reactions.filter(like_type='Dislike').count()
        return {'like': likes, 'dislike': dislikes}
