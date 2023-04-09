from django.urls import include, path

urlpatterns = [
    path('payment_accounts/', include('apps.payment_accounts.urls')),
    path('transactions/', include('apps.transactions.urls')),
    path('external_payments/', include('apps.external_payments.urls')),
]
