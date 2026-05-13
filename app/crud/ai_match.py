from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime

from app.models.doctor import Doctor
from app.models.availability import Availability
from app.models.appointment import Appointment
from app.utils.helpers import detect_specialization


def auto_book_by_symptoms(db: Session, patient_id: int, symptoms: str):
    specialization = detect_specialization(symptoms).strip()
    print("Detected specialization:", specialization)

    # Find doctor
    doctor = db.query(Doctor).filter(
        func.lower(func.trim(Doctor.specialization)) == specialization.lower()
    ).first()

    if not doctor:
        return {
            "message": "No matching doctor found",
            "doctor": None,
            "appointment": None
        }

    # Find next free slot
    slot = db.query(Availability).filter(
        Availability.doctor_id == doctor.id,
        Availability.is_booked == False
    ).order_by(Availability.available_date, Availability.slot_time).first()

    if not slot:
        return {
            "message": "Doctor found, but no slots available",
            "doctor": doctor,
            "appointment": None
        }

    # Create appointment automatically
    appointment = Appointment(
        patient_id=patient_id,
        doctor_id=doctor.id,
        appointment_date=datetime.combine(slot.available_date, datetime.min.time()),
        slot_time=slot.slot_time,
        reason=symptoms
    )

    db.add(appointment)

    # Mark slot booked
    slot.is_booked = True

    db.commit()
    db.refresh(appointment)

    return {
    "message": "Appointment booked successfully",

    "doctor": {
        "id": doctor.id,
        "specialization": doctor.specialization,
        "experience_years": doctor.experience_years,
        "consultation_fee": doctor.consultation_fee,
        "hospital_name": doctor.hospital_name,
        "hospital_address": doctor.hospital_address
    },

    "appointment": {
        "id": appointment.id,
        "patient_id": appointment.patient_id,
        "doctor_id": appointment.doctor_id,
        "appointment_date": appointment.appointment_date,
        "slot_time": appointment.slot_time,
        "reason": appointment.reason,
        "status": appointment.status,
        "created_at": appointment.created_at
    }
}