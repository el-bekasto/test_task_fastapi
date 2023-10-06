from pydantic import BaseModel, EmailStr, Field


class SendEmail(BaseModel):
    to: EmailStr
    subject: str = Field(default='Subject', max_length=70)
    message: str
