import uuid

from base.tokens.totp import BaseTOTPToken


class TOTPToken(BaseTOTPToken):
    @staticmethod
    def generate_totp() -> str:
        totp = str(uuid.uuid4())
        return totp
