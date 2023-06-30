from typing import Type

from base.models import BaseAbstractUser
from customer.models import CustomerUser
from developer.models import CompanyUser
from administrator.models import Admin


class DBModelFactory:
    def __init__(self):
        self._models = {}

    def register(self, app_label: str, model: BaseAbstractUser) -> None:
        # if not isinstance(model, BaseAbstractUser):
        #     raise TypeError('model must will be the "BaseAbstractUser" instance required!')
        self._models[app_label] = model

    def get_model(self, app_label: str) -> Type[BaseAbstractUser]:
        model = self._models.get(app_label)
        if not model:
            raise ValueError(f'User model from "{app_label}" is not registered!')
        return model


db_model_factory = DBModelFactory()
db_model_factory.register('customer', CustomerUser)
db_model_factory.register('developer', CompanyUser)
db_model_factory.register('administrator', Admin)
