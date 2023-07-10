from django.apps import AppConfig


class PaymentAcceptanceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.external_payments'
    verbose_name = 'Payment acceptance'

    def ready(self):
        from apps.external_payments import signals  # noqa: F401
