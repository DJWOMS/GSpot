from django.apps import AppConfig


class PaymentAcceptanceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.external_payments'
    verbose_name = 'Payment acceptance'
