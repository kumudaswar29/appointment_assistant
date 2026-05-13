from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.appointment import (
    AppointmentCreate,
    AppointmentUpdate,
    AppointmentResponse,
    AppointmentCancel
)
from app.crud.appointment import (
    create_appointment,
    get_appointments,
    get_appointment_by_id,
    get_appointments_by_doctor,
    get_appointments_by_patient,
    update_appointment,
    cancel_appointment
)
from app.crud.appointment import (
    create_appointment,
    get_appointments,
    get_appointment_by_id,
    get_appointments_by_doctor,
    get_appointments_by_patient,
    update_appointment,
    cancel_appointment
)

router = APIRouter(prefix="/appointments", tags=["Appointments"])


@router.post("/", response_model=AppointmentResponse)
def book_appointment(appointment: AppointmentCreate, db: Session = Depends(get_db)):
    return create_appointment(db, appointment)


@router.get("/", response_model=list[AppointmentResponse])
def all_appointments(db: Session = Depends(get_db)):
    return get_appointments(db)


@router.get("/{appointment_id}", response_model=AppointmentResponse)
def get_single_appointment(appointment_id: int, db: Session = Depends(get_db)):
    appointment = get_appointment_by_id(db, appointment_id)

    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")

    return appointment


@router.get("/doctor/{doctor_id}", response_model=list[AppointmentResponse])
def doctor_appointments(doctor_id: int, db: Session = Depends(get_db)):
    return get_appointments_by_doctor(db, doctor_id)


@router.get("/patient/{patient_id}", response_model=list[AppointmentResponse])
def patient_appointments(patient_id: int, db: Session = Depends(get_db)):
    return get_appointments_by_patient(db, patient_id)


@router.put("/{appointment_id}", response_model=AppointmentResponse)
def edit_appointment(
    appointment_id: int,
    appointment: AppointmentUpdate,
    db: Session = Depends(get_db)
):
    updated = update_appointment(db, appointment_id, appointment)

    if not updated:
        raise HTTPException(status_code=404, detail="Appointment not found")

    return updated

@router.put("/{appointment_id}/cancel", response_model=AppointmentResponse)
def cancel_existing_appointment(
    appointment_id: int,
    cancel_data: AppointmentCancel,
    db: Session = Depends(get_db)
):
    cancelled = cancel_appointment(
        db,
        appointment_id,
        cancel_data.cancelled_by,
        cancel_data.cancellation_reason
    )

    if not cancelled:
        raise HTTPException(status_code=404, detail="Appointment not found")

    return cancelled