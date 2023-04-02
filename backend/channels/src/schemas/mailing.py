from pydantic import BaseModel, EmailStr, HttpUrl


class EmailConfirm(BaseModel):
    confirm_email: EmailStr
    confirm_link: HttpUrl
