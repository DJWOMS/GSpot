from uuid import UUID

import requests
from config.celery import app
from django.conf import settings


@app.task()
def create_payment_account(user_uuid: UUID):
    url = f"{settings.PAYMENTS_DOMAIN}/api/v1/payment_accounts/create_account/"
    data = {"user_uuid": user_uuid}
    requests.post(url, data=data)
