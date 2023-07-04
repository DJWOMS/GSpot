from django.apps import AppConfig


class PaymentAccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.payment_accounts'
    verbose_name = 'Счета пользователя'

    def ready(self):
        import apps.payment_accounts.signals  # noqa: F401
