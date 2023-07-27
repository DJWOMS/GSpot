import os

from pydantic import BaseSettings


class SmtpConfig(BaseSettings):
    SMTP_HOST: str = os.environ.get('SMTP_HOST')
    SMTP_PORT: str = os.environ.get('SMTP_PORT')
    EMAIL_ADDRESS: str = os.environ.get('EMAIL_ADDRESS')
    EMAIL_PASSWORD: str = os.environ.get('EMAIL_PASSWORD')


smtp_config = SmtpConfig()
