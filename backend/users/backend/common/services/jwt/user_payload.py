from administrator.models import Admin
from base.models import BaseAbstractUser
from base.payload import BasePayload
from customer.models import CustomerUser
from developer.models import CompanyUser


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


class AdminPayload(BasePayload, CommonUserPayload):
    def __init__(self, user: BaseAbstractUser):
        self.user = user

    def generate_payload(self):
        common_payload = self.get_common_fields()
        return common_payload


class DeveloperPayload(BasePayload, CommonUserPayload):
    def __init__(self, user: BaseAbstractUser):
        self.user = user

    def generate_payload(self):
        common_payload = self.get_common_fields()
        return common_payload


class CustomerPayload(BasePayload, CommonUserPayload):
    def __init__(self, user: BaseAbstractUser):
        self.user = user

    def generate_payload(self):
        common_payload = self.get_common_fields()
        common_payload['age'] = self.user.age
        return common_payload


class PayloadFactory:
    payload_types = {
        Admin: AdminPayload,
        CompanyUser: DeveloperPayload,
        CustomerUser: CustomerPayload,
    }

    def create_payload(self, user_type: BaseAbstractUser) -> dict:
        payload_class = self.payload_types.get(user_type)
        if payload_class:
            return payload_class(user_type).generate_payload()
        else:
            raise ValueError("Unknown user type.")
