from common.services.totp import TOTPToken


class TOTPVerificationMixin:
    def perform_create(self, serializer):
        obj = serializer.save()
        TOTPToken().send_totp(obj)
