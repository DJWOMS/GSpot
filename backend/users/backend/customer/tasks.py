import requests
from celery import shared_task


@shared_task
def create_payment_account(user_uuid):
    url = "https://payments.alpha.g-spot.website/api/v1/payment_accounts/create_account/"
    data = {"user_uuid": user_uuid}
    response = requests.post(url, data=data)
    return response.json(), response.status_code
