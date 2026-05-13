from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class AppointmentCreate(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_date: datetime
    reason: Optional[str] = None


class AppointmentUpdate(BaseModel):
    status: Optional[str] = None
    appointment_date: Optional[datetime] = None

class AppointmentCancel(BaseModel):
    cancelled_by: str
    cancellation_reason: str

    
class AppointmentResponse(AppointmentCreate):
    id: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True