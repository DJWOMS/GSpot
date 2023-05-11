class InsufficientFundsError(Exception):
    pass


class NotPayoutDayError(Exception):
    pass


class PayOutLimitExceededError(Exception):
    pass


class NotValidAccountNumberError(Exception):
    pass
