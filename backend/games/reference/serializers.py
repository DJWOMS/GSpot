from rest_framework import serializers
from games.reference.models import Group, GroupElement


class GroupSerializer(serializers.ModelSerializer):
    type = serializers.ChoiceField(choices='')

    class Meta:
        model = Group
        fields = ('id', 'name', 'type')


class GroupElementSerializer(serializers.ModelSerializer):
    group = serializers.PrimaryKeyRelatedField()

    class Meta:
        model: GroupElement
        fields = ('id', 'name', 'group')
