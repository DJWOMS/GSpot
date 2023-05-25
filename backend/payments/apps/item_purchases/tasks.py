import requests
import rollbar
from apps.base.utils.change_balance import increase_user_balance
from apps.payment_accounts.models import Owner
from config.celery import app
from django.conf import settings
from requests.exceptions import RequestException

from .models import ItemPurchase, TransferHistory


@app.task
def get_item_for_self_user(item_purchase_id: int):
    item_purchase = ItemPurchase.objects.get(id=item_purchase_id)

    owner = Owner.objects.first()
    developer = item_purchase.developer_id

    developer_income = item_purchase.item_price.amount * ((100 - owner.commission) / 100)
    owner_income = item_purchase.item_price.amount * owner.commission / 100

    owner.withdraw_revenue(pk=owner.id, amount=item_purchase.item_price.amount)

    TransferHistory.objects.create(
        account_to=developer,
        amount=developer_income,
    )
    TransferHistory.objects.create(
        account_to=owner,
        amount=owner_income,
    )

    increase_user_balance(
        account=developer,
        amount=developer_income,
    )
    owner.deposit_income(
        pk=owner.id,
        amount=owner_income,
    )

    user = item_purchase.account_to
    refund_data = {'user': str(user.user_uuid), 'offer_uuid': str(item_purchase.item_uuid)}
    url = settings.GAMES_SERVICE.refund_url

    try:
        response = requests.post(url, json=refund_data)

        if response.status_code != requests.codes.CREATED:
            raise RequestException
    except RequestException as error:
        rollbar.report_message(
            f'Wrong response from games.'
            f'For user {user.user_uuid} with offer {item_purchase.item_uuid} '
            f'{error}',
            level='error',
        )

    item_purchase.status = ItemPurchase.ItemPurchaseStatus.PAID
    item_purchase.save()


@app.task
def gift_item_to_other_user():
    pass
