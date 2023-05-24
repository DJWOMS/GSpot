class DuplicateError(Exception):
    pass


class RefundNotAllowedError(Exception):
    def __init__(self, message='User is not eligible for a refund.'):
        self.message = message
        super().__init__(self.message)
