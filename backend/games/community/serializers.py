from rest_framework import serializers
from .models import Media, Social, Reviews, RewiewAnswers


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
        model = Reviews
        fields = ('game', 'text', 'grade')


class ReviewAnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = RewiewAnswers
        fields = ('review', 'text', 'grade')
