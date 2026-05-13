from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.patient import PatientCreate, PatientUpdate, PatientResponse
from app.crud.patient import (
    create_patient,
    get_patient_by_user_id,
    update_patient,
    get_patient_details
)
from app.models.patient import Patient

router = APIRouter(prefix="/patients", tags=["Patients"])


@router.get("/count")
def get_total_patients(db: Session = Depends(get_db)):
    total = db.query(Patient).count()
    return {"total_patients": total}


@router.post("/", response_model=PatientResponse)
def create_patient_profile(patient: PatientCreate, db: Session = Depends(get_db)):
    existing_patient = get_patient_by_user_id(db, patient.user_id)

    if existing_patient:
        raise HTTPException(status_code=400, detail="Patient profile already exists")

    return create_patient(db, patient)


@router.get("/details")
def get_all_patient_details(db: Session = Depends(get_db)):
    result = get_patient_details(db)
    return {"patients": [dict(r._mapping) for r in result]}


@router.get("/{user_id}", response_model=PatientResponse)
def get_patient_profile(user_id: int, db: Session = Depends(get_db)):
    patient = get_patient_by_user_id(db, user_id)

    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    return patient


@router.put("/{user_id}", response_model=PatientResponse)
def update_patient_profile(user_id: int, patient: PatientUpdate, db: Session = Depends(get_db)):
    updated_patient = update_patient(db, user_id, patient)

    if not updated_patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    return updated_patient