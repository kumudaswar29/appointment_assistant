from sqlalchemy.orm import Session
from app.models.availability import Availability
from app.schemas.availability import AvailabilityCreate


def create_availability(db: Session, data: AvailabilityCreate):
    slot = Availability(
        doctor_id=data.doctor_id,
        available_date=data.available_date,
        slot_time=data.slot_time,
        is_booked=False
    )
    db.add(slot)
    db.commit()
    db.refresh(slot)
    return slot


def get_doctor_availability(db: Session, doctor_id: int):
    return db.query(Availability).filter(
        Availability.doctor_id == doctor_id
    ).all()


def get_next_available_slot(db: Session, doctor_id: int):
    return db.query(Availability).filter(
        Availability.doctor_id == doctor_id,
        Availability.is_booked == False
    ).order_by(Availability.available_date, Availability.slot_time).first()


def mark_slot_booked(db: Session, slot_id: int):
    slot = db.query(Availability).filter(Availability.id == slot_id).first()

    if not slot:
        return None

    slot.is_booked = True
    db.commit()
    db.refresh(slot)
    return slot