from rest_framework import serializers

from base.choices import GradeChoices

from .models import Media, Social, Review, Comment, Reaction


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
    user_uuid = serializers.UUIDField()

    class Meta:
        model = Reaction
        fields = ('user_uuid', 'review', 'like_type')


class ReviewSerializer(serializers.ModelSerializer):
    reactions = serializers.SerializerMethodField()
    language = serializers.StringRelatedField()

    class Meta:
        model = Review
        exclude = ('game', )

    def get_reactions(self, obj):
        reactions = Reaction.objects.filter(review=obj)
        likes = reactions.filter(like_type=GradeChoices.LIKE).count()
        dislikes = reactions.filter(like_type=GradeChoices.DISLIKE).count()
        return {'like': likes, 'dislike': dislikes}
