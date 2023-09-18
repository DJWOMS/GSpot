from django.forms import ValidationError
from django.utils import timezone


def correct_date(from_dttm, to_dttm):
    if from_dttm < timezone.now() or from_dttm >= to_dttm:
        raise ValidationError(
            {'from_dttm': "from_dttm should more than current time and less than to_dttm"})
