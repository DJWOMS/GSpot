from decimal import Decimal
from typing import assert_never

import rollbar
from apps.base.utils.change_balance import increase_user_balance
from apps.payment_accounts.models import Owner
from config.celery import app
from django.core.exceptions import MultipleObjectsReturned
from django.db import transaction
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response

from ...base.classes import DRFtoDataClassMixin
from ...base.exceptions import DifferentStructureError
from ..exceptions import RefundNotAllowedError
from ..models import Invoice, ItemPurchase, ItemPurchaseHistory, TransferHistory
from ..schemas import ItemPurchaseData


class ItemPurchaseCompleter:
    def __init__(self, item_purchase: ItemPurchase, is_gift: bool = False):
        self.is_gift = is_gift
        self.item_purchase = item_purchase
        self._validate_income_data()

    def _validate_income_data(self):
        invoice = Invoice.objects.get(item_purchases=self.item_purchase)

        if (
            self.item_purchase.status != ItemPurchase.ItemPurchaseStatus.PENDING
            or invoice.is_paid is not True
        ):
            raise RefundNotAllowedError
        if (
            self.is_gift is True
            and self.item_purchase.account_from == self.item_purchase.account_to
        ):
            raise RefundNotAllowedError

    def take_refund(self):
        app.control.revoke(self.item_purchase.id, terminate=True)
        self.cancel_payment()

    def cancel_payment(self):
        owner = Owner.objects.first()

        with transaction.atomic():
            item_purchase_amount = self.item_purchase.item_price.amount
            increase_user_balance(
                account=self.item_purchase.account_from,
                amount=self.item_purchase.item_price.amount,
            )
            owner.withdraw_revenue(
                owner.pk,
                amount=item_purchase_amount,
            )
            self.item_purchase.status = ItemPurchase.ItemPurchaseStatus.REFUNDED
            self.item_purchase.save()

            ItemPurchaseHistory.objects.create(
                item_purchase_id=self.item_purchase,
                event_type=ItemPurchaseHistory.ItemPurchaseType.COMPLETED,
            )
            TransferHistory.objects.create_transfer_history(
                account_from=owner,
                account_to=self.item_purchase.account_from,
                amount=item_purchase_amount,
            )

    def accept_gift(self):
        app.control.revoke(self.item_purchase.id, terminate=True)
        self.accept_payment()

    def accept_payment(self):
        owner = Owner.objects.first()
        developer_income, owner_income = self._calculate_income_parts(self.item_purchase, owner)
        developer = self.item_purchase.developer_id

        with transaction.atomic():
            owner.withdraw_revenue(pk=owner.id, amount=self.item_purchase.item_price.amount)

            TransferHistory.objects.create_transfer_history(
                account_from=owner,
                account_to=developer,
                amount=developer_income,
            )
            TransferHistory.objects.create_transfer_history(
                account_to=owner,
                account_from=owner,
                amount=owner_income,
            )
            ItemPurchaseHistory.objects.create(
                item_purchase_id=self.item_purchase,
                event_type=ItemPurchaseHistory.ItemPurchaseType.COMPLETED,
            )

            increase_user_balance(
                account=developer,
                amount=developer_income,
            )
            owner.deposit_income(
                pk=owner.id,
                amount=owner_income,
            )

            self.item_purchase.status = ItemPurchase.ItemPurchaseStatus.PAID
            self.item_purchase.save()

    @staticmethod
    def _calculate_income_parts(
        item_purchase: ItemPurchase,
        owner: Owner,
    ) -> tuple[Decimal, Decimal]:
        developer_income = item_purchase.item_price.amount * ((100 - owner.commission) / 100)
        owner_income = item_purchase.item_price.amount * owner.commission / 100
        return developer_income, owner_income


class ItemPurchaseStatusChanger(DRFtoDataClassMixin):
    def update_item_purchase_status(
        self,
        request: Request,
        event_type: ItemPurchase.ItemPurchaseStatus,
    ) -> Response:
        """
        Status ItemPurchaseStatus.PAID - using only when it's gift
        Status ItemPurchaseStatus.REFUNDED - using when it's refund case for gift and for self
        """
        try:
            item_purchase_data = self.convert_data(request, ItemPurchaseData)
        except DifferentStructureError:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        response = self.fetch_item_purchase(item_purchase_data)
        if type(response) != ItemPurchase:
            return response

        data = {'item_purchase': response}
        if event_type == ItemPurchase.ItemPurchaseStatus.PAID:
            data['is_gift'] = True
        try:
            item_purchase_processor = ItemPurchaseCompleter(**data)
        except RefundNotAllowedError as error:
            return Response(
                {'detail': str(error)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        match event_type:
            case ItemPurchase.ItemPurchaseStatus.PAID:
                item_purchase_processor.accept_gift()
                return Response(status=status.HTTP_200_OK)

            case ItemPurchase.ItemPurchaseStatus.REFUNDED:
                item_purchase_processor.take_refund()
                return Response(status=status.HTTP_202_ACCEPTED)

            case _ as not_implemented:
                assert_never(not_implemented)

    def fetch_item_purchase(self, item_purchase_data: ItemPurchaseData) -> ItemPurchase | Response:
        try:
            item_purchase = ItemPurchase.objects.get(
                account_to__user_uuid=item_purchase_data.user_uuid_to,
                account_from__user_uuid=item_purchase_data.user_uuid_from,
                item_uuid=item_purchase_data.item_uuid,
                status=ItemPurchase.ItemPurchaseStatus.PENDING,
            )
        except ItemPurchase.DoesNotExist:
            return Response(
                {'detail': 'No such product for this user'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except MultipleObjectsReturned:
            rollbar.report_message(
                'Found several ItemPurchase instances while trying to update status '
                'for next query conditions: '
                f'account_to__user_uuid={item_purchase_data.user_uuid}, '
                f'item_uuid={item_purchase_data.item_uuid}, '
                f'status={ItemPurchase.ItemPurchaseStatus.PENDING} ',
                'error',
            )
            return Response(
                {'detail': 'internal server error'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        return item_purchase
