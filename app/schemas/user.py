from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    full_name: str
    email: EmailStr
    phone: str
    role: Optional[str] = "patient"

    @field_validator("full_name")
    def validate_full_name(cls, value):

        if not value.strip():
            raise ValueError("Full Name is required")

        return value

    @field_validator("phone")
    def validate_phone(cls, value):

        if not value.strip():
            raise ValueError("Phone number is required")

        if not value.isdigit():
            raise ValueError("Phone number must contain only digits")

        if len(value) != 10:
            raise ValueError("Phone number must be exactly 10 digits")

        return value

    @field_validator("role")
    def validate_role(cls, value):

        if not value.strip():
            raise ValueError("Role is required")

        # Public registration allowed roles only
        allowed_roles = ["patient", "doctor"]

        if value.lower() not in allowed_roles:
            raise ValueError("Invalid role")

        return value


class UserCreate(UserBase):
    password: str

    @field_validator("password")
    def validate_password(cls, value):

        if not value.strip():
            raise ValueError("Password is required")

        if len(value) < 6:
            raise ValueError("Password must be at least 6 characters long")

        return value


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