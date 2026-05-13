from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional


class PatientBase(BaseModel):
    gender: str
    date_of_birth: date
    blood_group: Optional[str] = None
    address: Optional[str] = None
    emergency_contact: Optional[str] = None


class PatientCreate(PatientBase):
    user_id: int


class PatientUpdate(BaseModel):
    gender: Optional[str] = None
    date_of_birth: Optional[date] = None
    blood_group: Optional[str] = None
    address: Optional[str] = None
    emergency_contact: Optional[str] = None


class PatientResponse(PatientBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True