from abc import ABC, abstractmethod


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
