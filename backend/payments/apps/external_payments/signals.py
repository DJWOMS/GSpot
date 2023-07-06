from apps.external_payments.models import PaymentCommission
from django.core.cache import cache
from django.db import models
from django.dispatch import receiver


@receiver(models.signals.post_save, sender=PaymentCommission)
def update_cache(sender, instance: PaymentCommission, **kwargs):
    cache.set(instance.cache_key, instance.commission)
