from typing import Union

from django.db.models import (
    CharField,
    DecimalField,
    IntegerChoices,
    PositiveSmallIntegerField,
    TextChoices,
)


def get_field_from_choices(
    label, choices_class: Union[IntegerChoices, TextChoices], **kwargs
) -> Union[PositiveSmallIntegerField, CharField]:
    """Get django model field from choices class"""

    if issubclass(choices_class, IntegerChoices):
        return PositiveSmallIntegerField(label, choices=choices_class.choices, **kwargs)
    elif issubclass(choices_class, TextChoices):
        if "max_length" in kwargs:
            max_length = kwargs.pop("max_length")
        else:
            max_length = max([len(v) for v in choices_class.values])

        return CharField(
            label, choices=choices_class.choices, max_length=max_length, **kwargs
        )
    else:
        raise AssertionError(
            "Unexpected choice class. Must be of IntegerChoices or TextChoices"
        )


class AmountField(DecimalField):
    def __init__(
        self, verbose_name=None, name=None, max_digits=10, decimal_places=2, **kwargs
    ):
        super().__init__(verbose_name, name, max_digits, decimal_places, **kwargs)
