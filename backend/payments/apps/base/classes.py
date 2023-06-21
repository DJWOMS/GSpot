from abc import ABC, abstractmethod

import rollbar
from apps.base.exceptions import DifferentStructureError
from dacite import from_dict


class AbstractPaymentService(ABC):
    @abstractmethod
    def request_balance_deposit_url(self, payment_data):
        pass

    @abstractmethod
    def handel_payment_response(self):
        pass

    @abstractmethod
    def parse_income_data(self, **kwargs):
        pass

    @abstractmethod
    def validate_income_data(self, parsed_data):
        pass


class AbstractPayoutService(ABC):
    @abstractmethod
    def request_payout(self, payout_data):
        pass


class DRFtoDataClassMixin:
    def convert_data(self, request, dataclass_model):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self.__convert_drf_to_dataclass(dataclass_model, serializer)

    def __convert_drf_to_dataclass(self, data_model, serializer: dict):
        # TODO change to pydantic, add typehint for pydantic model  # noqa: T000
        try:
            data_model_data = from_dict(
                data_model,
                serializer.validated_data,
            )
        except AttributeError:
            data_model_data = data_model(**serializer.validated_data)
        except KeyError as error:
            rollbar.report_message(
                f'Schemas and serializers got different structure. Got next error: {str(error)}',
                'error',
            )
            raise DifferentStructureError
        return data_model_data
