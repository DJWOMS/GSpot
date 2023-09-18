from django.db.models import Count

from rest_framework import serializers

from .models import Media, Social, Review, Comment, Reaction, Language


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'


class GameSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ('type', 'url')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ('review', )


class ReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = ('id', 'like_type')


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    reactions = serializers.SerializerMethodField()
    language = LanguageSerializer

    class Meta:
        model = Review
        fields = '__all__'

    def get_reactions(self, obj):
        reactions = Reaction.objects.filter(review=obj)
        likes = reactions.filter(like_type='Like').count()
        dislikes = reactions.filter(like_type='Dislike').count()
        return {'like': likes, 'dislike': dislikes}
