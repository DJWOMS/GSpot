from rest_framework import serializers
from games.reference.models import Group


class GroupSerializer(serializers.ModelSerializer):
    type = serializers.ChoiceField(choices='какой-то choices написать после создания модели')

    class Meta:
        model = Group
        fields = ('id', 'name', 'type')
