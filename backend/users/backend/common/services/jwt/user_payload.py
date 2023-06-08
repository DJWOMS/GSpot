from base.models import BaseAbstractUser


class PayloadFactory:
    payload_types = {}

    def create_payload(self, user_type: BaseAbstractUser) -> dict:
        payload_class = self.payload_types.get(user_type)
        if payload_class:
            return payload_class.generate_payload()
        else:
            raise ValueError("Unknown user type.")
