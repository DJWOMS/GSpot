from abc import ABC, abstractmethod

import rollbar
from apps.base.exceptions import DifferentStructureError


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


class DRFtoDataClassConverter:
    def convert_data(self, request, dataclass_model):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self.__convert_drf_to_dataclass(dataclass_model, serializer.validated_data)

    def __convert_drf_to_dataclass(self, dataclass_model, serializer_data: dict):
        # TODO change to pydantic, add typehint for pydantic model  # noqa: T000
        try:
            dataclass_data = dataclass_model(
                **serializer_data,
            )
        except KeyError as error:
            rollbar.report_message(
                f'Schemas and serializers got different structure. Got next error: {str(error)}',
                'error',
            )
            raise DifferentStructureError
        return dataclass_data
