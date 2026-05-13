from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class DoctorBase(BaseModel):
    specialization: str
    experience_years: int
    consultation_fee: int
    hospital_name: str
    hospital_address: Optional[str] = None


class DoctorCreate(DoctorBase):
    user_id: int


class DoctorUpdate(BaseModel):
    specialization: Optional[str] = None
    experience_years: Optional[int] = None
    consultation_fee: Optional[int] = None
    hospital_name: Optional[str] = None
    hospital_address: Optional[str] = None


class DoctorResponse(DoctorBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True