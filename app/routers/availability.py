from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.availability import AvailabilityCreate, AvailabilityResponse
from app.crud.availability import (
    create_availability,
    get_doctor_availability,
    mark_slot_booked
)

router = APIRouter(prefix="/availability", tags=["Availability"])


@router.post("/", response_model=AvailabilityResponse)
def add_availability(data: AvailabilityCreate, db: Session = Depends(get_db)):
    return create_availability(db, data)


@router.get("/{doctor_id}")
def doctor_availability(doctor_id: int, db: Session = Depends(get_db)):
    return get_doctor_availability(db, doctor_id)


@router.put("/book/{slot_id}")
def book_slot(slot_id: int, db: Session = Depends(get_db)):
    slot = mark_slot_booked(db, slot_id)

    if not slot:
        raise HTTPException(status_code=404, detail="Slot not found")

    return {"message": "Slot booked successfully", "slot": slot}