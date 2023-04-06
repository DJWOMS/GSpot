from typing import List, Any

from pydantic import BaseModel, EmailStr, HttpUrl, validator


class EmailConfirm(BaseModel):
    confirm_email: EmailStr
    confirm_link: HttpUrl


class MassageMail(BaseModel):
    subject: str
    template_name: str
    recipients: List[EmailStr]
    template_body: dict

    @validator('template_name')
    def validate_template_name(cls, template_name: str) -> str:
        if not template_name.endswith('.html'):
            raise ValueError('Template name must end with .html')
        return template_name
