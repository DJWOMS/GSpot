from administrator.models import Admin
from base.models import BaseAbstractUser
from customer.models import CustomerUser
from developer.models import CompanyUser
from rest_framework.serializers import ModelSerializer


class CustomerTOTPSerializer(ModelSerializer):
    class Meta:
        model = CustomerUser
        field = '__all__'
        exclude = ('password',)


class CompanyUserTOTPSerializer(ModelSerializer):
    class Meta:
        model = CompanyUser
        field = '__all__'
        exclude = ('password',)


class AdminTOTPSerializer(ModelSerializer):
    class Meta:
        model = Admin
        field = '__all__'
        exclude = ('password',)


class DBModelFactory:
    def __init__(self):
        self._models = {}

    def register(
        self,
        app_label: str,
        model: BaseAbstractUser,
        serializer: ModelSerializer,
    ) -> None:
        if not issubclass(model, BaseAbstractUser):
            raise TypeError('Model must will be the "BaseAbstractUser" instance required!')
        self._models[app_label] = (model, serializer)

    def get_models(self, app_label: str) -> tuple[type[BaseAbstractUser], type[ModelSerializer]]:
        model = self._models.get(app_label)
        if not model:
            raise ValueError(f'Models for "{app_label}" is not registered!')
        return model


db_model_factory = DBModelFactory()
db_model_factory.register('customer', CustomerUser, CustomerTOTPSerializer)
db_model_factory.register('developer', CompanyUser, CompanyUserTOTPSerializer)
db_model_factory.register('administrator', Admin, AdminTOTPSerializer)
