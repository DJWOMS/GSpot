from decimal import ROUND_HALF_DOWN, Decimal

from apps.base.schemas import PaymentTypes
from apps.external_payments.models import PaymentCommission, PaymentService
from django.core.cache import cache
from django.shortcuts import get_object_or_404


class PaymentCalculation:
    TWO_PLACES = Decimal(10) ** -2

    def __init__(
        self,
        payment_type: PaymentTypes,
        payment_service: PaymentService,
        payment_amount: Decimal,
    ):
        self.payment_type = payment_type
        self.payment_service = payment_service
        self.payment_amount = payment_amount
        self.key_cache = f'unique_key_{payment_service.name}_{payment_type.name}'

    def calculate_payment_with_commission(self) -> Decimal:
        commission = self._get_commission_percent()
        return (self.payment_amount * (1 / (1 - commission / 100))).quantize(
            self.TWO_PLACES,
            ROUND_HALF_DOWN,
        )

    def calculate_payment_without_commission(self) -> Decimal:
        commission = self._get_commission_percent()
        return (self.payment_amount * ((100 - commission) / 100)).quantize(
            self.TWO_PLACES,
            ROUND_HALF_DOWN,
        )

    def _get_commission_percent(self) -> Decimal:
        if result := cache.get(self.key_cache):
            return result

        payment_commission = get_object_or_404(
            PaymentCommission,
            payment_type=self.payment_type.name,
            payment_service_id__name=self.payment_service.name,
        )

        cache.set(self.key_cache, payment_commission.commission)
        return payment_commission.commission
