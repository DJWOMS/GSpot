from administrator.models import Admin
from base.models import BaseAbstractUser
from base.tokens.payload import BasePayload
from customer.models import CustomerUser
from developer.models import CompanyUser


class CommonUserPayload:
    def __init__(self):
        self.user = None

    def get_common_payload(self) -> dict:
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
        common_payload = self.get_common_payload()
        return common_payload


class DeveloperPayload(BasePayload, CommonUserPayload):
    def __init__(self, user: BaseAbstractUser):
        self.user = user

    def generate_payload(self):
        common_payload = self.get_common_payload()
        return common_payload


class CustomerPayload(BasePayload, CommonUserPayload):
    def __init__(self, user: BaseAbstractUser):
        self.user = user

    def generate_payload(self):
        common_payload = self.get_common_payload()
        common_payload['age'] = self.user.age
        return common_payload


class PayloadFactory:
    payload_types = {
        Admin: AdminPayload,
        CompanyUser: DeveloperPayload,
        CustomerUser: CustomerPayload,
    }

    def create_payload(self, user: BaseAbstractUser) -> dict:
        if isinstance(user, BaseAbstractUser):
            return self.create_payload_for_user(user)
        else:
            raise TypeError('BaseAbstractUser instance required!')

    def create_payload_for_user(self, user: BaseAbstractUser) -> dict:
        user_type = type(user)
        payload_class = self.payload_types.get(user_type)
        if payload_class:
            return payload_class(user).generate_payload()
        else:
            raise KeyError("Unknown user type!")
