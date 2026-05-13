from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.doctor import DoctorCreate, DoctorUpdate, DoctorResponse
from app.crud.doctor import create_doctor, get_doctor_by_user_id, update_doctor

router = APIRouter(prefix="/doctors", tags=["Doctors"])


@router.post("/", response_model=DoctorResponse)
def create_doctor_profile(doctor: DoctorCreate, db: Session = Depends(get_db)):
    existing = get_doctor_by_user_id(db, doctor.user_id)

    if existing:
        raise HTTPException(status_code=400, detail="Doctor already exists")

    return create_doctor(db, doctor)


@router.get("/{user_id}", response_model=DoctorResponse)
def get_doctor_profile(user_id: int, db: Session = Depends(get_db)):
    doctor = get_doctor_by_user_id(db, user_id)

    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    return doctor


@router.put("/{user_id}", response_model=DoctorResponse)
def update_doctor_profile(user_id: int, doctor: DoctorUpdate, db: Session = Depends(get_db)):
    updated = update_doctor(db, user_id, doctor)

    if not updated:
        raise HTTPException(status_code=404, detail="Doctor not found")

    return updated