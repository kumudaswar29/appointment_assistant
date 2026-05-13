from pydantic import BaseModel
from datetime import date


class AvailabilityCreate(BaseModel):
    doctor_id: int
    available_date: date
    slot_time: str


class AvailabilityResponse(BaseModel):
    id: int
    doctor_id: int
    available_date: date
    slot_time: str
    is_booked: bool

    class Config:
        from_attributes = True