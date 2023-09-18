from rest_framework import serializers
from django.db.models import Model


class ChoiceAsDictField(serializers.ChoiceField):
    """
    Serializes field with choices as a dictionary to provide both value and label of the choice.
    """

    def to_representation(self, value):
        if value in ("", None):
            return None
        return {"id": value, "label": self.choices[value]}


class BaseModelSerializer(serializers.ModelSerializer):
    """
    A base ModelSerializer used by default in the project. Extends default ModelSerializer by:
    * using custom serialization for choice fields
    """
    serializer_choice_field = ChoiceAsDictField

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if (
            getattr(self.Meta, "fields", None) is None
            and getattr(self.Meta, "exclude", None) is None
        ):
            setattr(self.Meta, "fields", "__all__")

    class Meta:
        model: Model
