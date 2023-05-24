from apps.base.utils.change_balance import increase_user_balance
from apps.payment_accounts.models import Account
from config.celery import app

from ..exceptions import RefundNotAllowedError
from ..models import Invoice, ItemPurchase, ItemPurchaseHistory
from ..schemas import RefundData


class RefundProcessor:
    def __init__(self, refund_data: RefundData):
        self.user_uuid = refund_data.user_uuid
        self.item_uuid = refund_data.offer_uuid
        self._validate_income_data()

    def _validate_income_data(self):
        try:
            self.user_account = Account.objects.get(user_uuid=self.user_uuid)
        except Account.DoesNotExist:
            raise Account.DoesNotExist('This user does not exist.')

        try:
            self.item_purchase = ItemPurchase.objects.filter(
                account_to=self.user_account,
                item_uuid=self.item_uuid,
            ).last()
        except ItemPurchase.DoesNotExist:
            raise ItemPurchase.DoesNotExist('No such product in this user.')

        invoice = Invoice.objects.get(item_purchases=self.item_purchase)

        if self.item_purchase.status != 'PENDING' or invoice.is_paid is not True:
            raise RefundNotAllowedError

    def take_refund(self):
        app.control.revoke(self.item_purchase.id, terminate=True)

        increase_user_balance(
            account=self.user_account,
            amount=self.item_purchase.item_price.amount,
        )
        self.item_purchase.status = ItemPurchase.ItemPurchaseStatus.REFUNDED
        self.item_purchase.save()

        ItemPurchaseHistory.objects.create(
            item_purchase_id=self.item_purchase,
            event_type=ItemPurchaseHistory.ItemPurchaseType.COMPLETED,
        )
