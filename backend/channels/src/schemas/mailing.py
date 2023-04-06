from typing import List, Any

from pydantic import BaseModel, EmailStr, HttpUrl, validator


class EmailConfirm(BaseModel):
    confirm_email: EmailStr
    confirm_link: HttpUrl


class MassageMail(BaseModel):
    subject: str
    template_name: str
    recipients: List[EmailStr]
    template_body: dict[HttpUrl | Any]

    @validator("template_name")
    def mast_be_html_extends(self, v):
        if v.split('.')[-1] == 'html':
            return v
        else:
            raise ValueError('invalid template format. Supports only .html')

