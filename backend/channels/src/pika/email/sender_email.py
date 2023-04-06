from pathlib import Path

from fastapi_mail import ConnectionConfig, MessageSchema, FastMail, MessageType

from schemas.mailing import EmailConfirm
from config import settings

from src.schemas.mailing import MassageMail


class Sender:
    def __init__(self):
        self.__conf = ConnectionConfig(
            MAIL_USERNAME=settings.EMAIL_HOST_USER,
            MAIL_PASSWORD=settings.EMAIL_HOST_PASSWORD,
            MAIL_FROM=settings.EMAIL_HOST_USER,
            MAIL_PORT=settings.EMAIL_PORT,
            MAIL_SERVER=settings.EMAIL_HOST,
            MAIL_STARTTLS=False,
            MAIL_SSL_TLS=True,
            TEMPLATE_FOLDER=Path(__file__).parent / 'templates',
        )

    async def __send(self, subject, recipients, template_body, template_name):
        message = MessageSchema(
            subject=subject,
            recipients=recipients,
            template_body=template_body,
            subtype=MessageType.html,
        )

        fm = FastMail(self.__conf)
        await fm.send_message(message, template_name=template_name)

    @staticmethod
    def get_data_by_type(type_msg, body) -> MassageMail:
        match type_msg:
            case 'test_queue':
                serializer = EmailConfirm(**body).dict()
                massage_data = {
                    'subject': 'Confirm Email',
                    'template_name': 'confirm_email.html',
                    'recipients': [serializer.pop('confirm_email')],
                    'template_body': serializer
                }
                return MassageMail(**massage_data)

    async def send_email(self, type_msg, body):
        massage_data = self.get_data_by_type(
            type_msg=type_msg,
            body=body
        )
        await self.__send(
            subject=massage_data.subject,
            recipients=massage_data.recipients,
            template_name=massage_data.template_name,
            template_body=massage_data.template_body,
        )


sender = Sender()
