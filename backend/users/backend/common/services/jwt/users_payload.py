from administrator.models import Admin
from base.models import BaseAbstractUser
from base.tokens.payload import BasePayload
from customer.models import CustomerUser
from developer.models import CompanyUser
from django.forms import model_to_dict


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
        admin_payload = {
            "email": self.user.email,
            "phone": self.user.phone,
            "country": self.user.country,
            "created_at": str(self.user.created_at),
            "update_at": str(self.user.update_at),
            "is_superuser": self.user.is_superuser,
            "groups": list(self.user.groups.all()),
            "user_permissions": list(self.user.user_permissions.all()),
            "developer_groups": list(self.user.developer_groups.all()),
            "developer_permissions": list(self.user.developer_permissions.all()),
        }
        payload = common_payload | admin_payload

        return payload


class DeveloperPayload(BasePayload, CommonUserPayload):
    def __init__(self, user: BaseAbstractUser):
        self.user = user

    def generate_payload(self):
        common_payload = self.get_common_payload()
        company = {}
        if self.user.company is not None:
            company = model_to_dict(self.user.company)
            company['created_by'] = str(company['created_by'])
            company['image'] = str(self.user.company.image)
        developer_payload = {
            "email": self.user.email,
            "phone": self.user.phone,
            "country": self.user.country,
            "created_at": str(self.user.created_at),
            "update_at": str(self.user.update_at),
            "is_active": self.user.is_active,
            "is_superuser": self.user.is_superuser,
            "groups": list(self.user.groups.all()),
            "user_permissions": list(self.user.user_permissions.all()),
            "company": company,
        }
        payload = common_payload | developer_payload
        return payload


class CustomerPayload(BasePayload, CommonUserPayload):
    def __init__(self, user: BaseAbstractUser):
        self.user = user

    def generate_payload(self):
        common_payload = self.get_common_payload()
        common_payload["age"] = self.user.age
        customer_payload = {
            "email": self.user.email,
            "phone": self.user.phone,
            "created_at": str(self.user.created_at),
            "update_at": str(self.user.update_at),
            "friends": list(self.user.friends.all()),
            "birthday": str(self.user.birthday),
            "is_active": self.user.is_active,
            "country": self.user.country,
        }
        payload = common_payload | customer_payload

        return payload


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
            raise TypeError("BaseAbstractUser instance required!")

    def create_payload_for_user(self, user: BaseAbstractUser) -> dict:
        user_type = type(user)
        payload_class = self.payload_types.get(user_type)
        if payload_class:
            return payload_class(user).generate_payload()
        else:
            raise KeyError("Unknown user type!")
