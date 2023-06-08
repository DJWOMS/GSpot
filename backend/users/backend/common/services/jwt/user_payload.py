from base.models import BaseAbstractUser


class CommonUserPayload:
    def __init__(self):
        self.user = None

    def get_common_fields(self) -> dict:
        common_payload = {
            "user_id": str(self.user.id),
            "role": self.user._meta.app_label,
            "avatar": str(self.user.avatar),
            "permissions": self.user.permissions_codename,
        }
        return common_payload


class PayloadFactory:
    payload_types = {}

    def create_payload(self, user_type: BaseAbstractUser) -> dict:
        payload_class = self.payload_types.get(user_type)
        if payload_class:
            return payload_class.generate_payload()
        else:
            raise ValueError("Unknown user type.")
