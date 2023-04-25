from django.apps import AppConfig


class PaymentAccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.payment_accounts'
    verbose_name = 'Счета пользователя'
