from typing import TypeVar

import rollbar
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Model

DjangoModel = TypeVar('DjangoModel', bound=Model)


def parse_model_instance(
        *,
        django_model: type[DjangoModel],
        error_message: str,
        pk: int,
) -> DjangoModel | None:
    try:
        django_model_instance = django_model.objects.get(id=pk)
    except ObjectDoesNotExist:
        rollbar.report_message(error_message, 'warning')
        return None

    return django_model_instance
