from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    full_name: str
    email: EmailStr
    phone: str
    role: Optional[str] = "patient"

    @field_validator("phone")
    def validate_phone(cls, value):
        if not value.isdigit():
            raise ValueError("Phone number must contain only digits")

        if len(value) != 10:
            raise ValueError("Phone number must be exactly 10 digits")

        return value


class UserCreate(UserBase):
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(UserBase):
    id: int
    is_active: bool
    is_verified: bool
    created_at: datetime

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    access_token: str
    token_type: str