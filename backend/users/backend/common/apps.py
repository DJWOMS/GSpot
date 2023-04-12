from django.apps import AppConfig
from django.contrib import admin


class BaseAppConfig(AppConfig):
    def ready(self):
        # Automatically register in admin all models
        # importing from here to not face error - apps not loaded yet

        admin_class = type("AdminClass", (admin.ModelAdmin,), {})
        models = self.get_models()
        for model in models:
            if not admin.site.is_registered(model):
                admin.site.register(model, admin_class)
