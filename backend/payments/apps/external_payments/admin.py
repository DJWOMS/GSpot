from apps.base.utils.classmethod import register_admin_classes
from django.apps import apps

models = apps.get_models()
register_admin_classes(models)
