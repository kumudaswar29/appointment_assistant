from datetime import datetime
from sqlalchemy.orm import Session
from app.models.appointment import Appointment
from app.schemas.appointment import AppointmentCreate, AppointmentUpdate


def create_appointment(db: Session, data: AppointmentCreate):
    db_appointment = Appointment(**data.dict())
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment


def get_appointments(db: Session):
    return db.query(Appointment).all()


def get_appointment_by_id(db: Session, appointment_id: int):
    return db.query(Appointment).filter(Appointment.id == appointment_id).first()


def get_appointments_by_doctor(db: Session, doctor_id: int):
    return db.query(Appointment).filter(Appointment.doctor_id == doctor_id).all()


def get_appointments_by_patient(db: Session, patient_id: int):
    return db.query(Appointment).filter(Appointment.patient_id == patient_id).all()


def update_appointment(db: Session, appointment_id: int, appointment: AppointmentUpdate):
    db_appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()

    if not db_appointment:
        return None

    for key, value in appointment.dict(exclude_unset=True).items():
        setattr(db_appointment, key, value)

    db.commit()
    db.refresh(db_appointment)
    return db_appointment

def cancel_appointment(db: Session, appointment_id: int, cancelled_by: str, cancellation_reason: str):
    db_appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()

    if not db_appointment:
        return None

    db_appointment.status = "cancelled"
    db_appointment.cancelled_by = cancelled_by
    db_appointment.cancellation_reason = cancellation_reason
    db_appointment.cancelled_at = datetime.utcnow()

    db.commit()
    db.refresh(db_appointment)
    return db_appointment