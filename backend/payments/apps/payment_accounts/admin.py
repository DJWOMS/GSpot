from django.apps import apps

from apps.base.utils.classmethod import register_admin_classes


models = apps.get_models()
register_admin_classes(models)

