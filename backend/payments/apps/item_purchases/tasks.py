import requests
import rollbar
from config.celery import app
from django.conf import settings
from requests.exceptions import RequestException

from .exceptions import RefundNotAllowedError
from .models import ItemPurchase
from .services.item_purchase_completer import ItemPurchaseCompleter


@app.task
def get_item_for_self_user(item_purchase_id: int):
    try:
        item_purchase = ItemPurchase.objects.get(id=item_purchase_id)
    except ItemPurchase.DoesNotExist:
        rollbar.report_message(
            f'Cant find Item with id {item_purchase_id} to perform refund',
            level='error',
        )
        return

    try:
        item_purchase_processor = ItemPurchaseCompleter(item_purchase)
    except RefundNotAllowedError as error:
        rollbar.report_message(str(error), level='info')
        return
    item_purchase_processor.accept_payment()

    user = item_purchase.account_to
    refund_data = {'user_uuid': str(user.user_uuid), 'offer_uuid': str(item_purchase.item_uuid)}
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


@app.task
def cancel_gift_item(item_purchase_id: int) -> None:
    try:
        item_purchase = ItemPurchase.objects.get(id=item_purchase_id)
    except ItemPurchase.DoesNotExist:
        rollbar.report_message(
            f'Cant find Item with id {item_purchase_id} to perform refund',
            level='error',
        )
        return
    try:
        item_purchase_processor = ItemPurchaseCompleter(item_purchase=item_purchase, is_gift=True)
    except RefundNotAllowedError as error:
        rollbar.report_message(str(error), level='info')
        return
    item_purchase_processor.cancel_payment()

    cancel_gift_url = settings.GAMES_SERVICE.cancel_gift_url
    refund_data = {
        'user_uuid': str(item_purchase.account_to.user_uuid),
        'offer_uuid': str(item_purchase.item_uuid),
    }
    try:
        response = requests.post(cancel_gift_url, json=refund_data)
    except RequestException as error:
        rollbar.report_message(
            f'Wrong response from games.'
            f'For user {refund_data.user_uuid} with offer {refund_data.item_uuid} '
            f'{error}',
            level='error',
        )
    else:
        if response.status_code != requests.codes.CREATED:
            rollbar.report_message(
                f'Cant send cancel payment data to {cancel_gift_url}',
                level='error',
            )
