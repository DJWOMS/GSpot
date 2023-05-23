from django.conf import settings
from yookassa.client import ApiClient
from yookassa.domain.common import HttpVerb


def check_yookassa_response(yookassa_data: dict) -> bool:
    payment_id = yookassa_data.get('id')
    if payment_id is None:
        return False

    settings.YOOKASSA_CONFIG.get_payment_settings()
    client = ApiClient()
    base_path = '/payments'

    path = base_path + '/' + payment_id
    response = client.request(HttpVerb.GET, path)

    return response == yookassa_data
