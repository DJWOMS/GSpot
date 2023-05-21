from yookassa import Payment
from yookassa.domain.common import HttpVerb


class GetPaymentData(Payment):
    @classmethod
    def find_one(cls, payment_id):
        instance = cls()
        if not isinstance(payment_id, str) or not payment_id:
            raise ValueError('Invalid payment_id value')

        path = instance.base_path + '/' + payment_id
        response = instance.client.request(HttpVerb.GET, path)
        return response


def check_yookassa_response(yokassa_data: dict) -> bool:
    payment_data = GetPaymentData.find_one(yokassa_data['id'])
    if payment_data == yokassa_data:
        return True
    return False
