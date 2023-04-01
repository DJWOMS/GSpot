from djangorestframework_camel_case.parser import (
    CamelCaseFormParser,
    CamelCaseMultiPartParser,
)
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


def choices_to_dict(choices):
    if choices:
        return [{"id": k, "label": v} for k, v in choices]
    else:
        return None


class BaseModelViewSet(viewsets.ModelViewSet):
    """
    Extends default ModelViewSet by:
    * custom choices action to give info of model allowed choices
    * auto definition serializer many param
    """
    yasg_parser_classes = [CamelCaseFormParser, CamelCaseMultiPartParser]

    @action(methods=["GET"], detail=False)
    def choices(self, request):
        """ Get all available values for choice fields """
        qs = self.get_queryset()
        model_fields = qs.model._meta.fields

        field_choices = {
            field.name: choices_to_dict(field.choices)
            for field in model_fields
            if hasattr(field, "choices") and field.choices is not None
        }

        return Response(field_choices)

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data", {}), list):
            kwargs["many"] = True
            serializer = super().get_serializer(*args, **kwargs)
            serializer.is_valid()
        else:
            serializer = super().get_serializer(*args, **kwargs)
        return serializer
