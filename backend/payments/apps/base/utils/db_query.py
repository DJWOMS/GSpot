from apps.base.utils.change_balance import DjangoModel
from django.http import Http404


def multiple_select_or_404(
    data_list: list,
    django_model: type[DjangoModel],
    look_up_field: str,
) -> list[DjangoModel] | None:
    """Main purpose of this function to prevent sending multiple get_object_or_404 to database"""
    field_name = f'{look_up_field}__in'
    query = list(django_model.objects.filter(**{field_name: data_list}))

    if len(query) != len(set(data_list)):
        missing_attrs = set(data_list) - {getattr(obj, look_up_field) for obj in query}
        raise Http404(
            f'Field {look_up_field} with next values {missing_attrs} not found in database.',
        )
    return query
