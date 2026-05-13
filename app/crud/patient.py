from sqlalchemy import text
from sqlalchemy.orm import Session
from app.models.patient import Patient
from app.schemas.patient import PatientCreate, PatientUpdate


def create_patient(db: Session, patient: PatientCreate):
    db_patient = Patient(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient


def get_patient_by_user_id(db: Session, user_id: int):
    return db.query(Patient).filter(Patient.user_id == user_id).first()


def update_patient(db: Session, user_id: int, patient: PatientUpdate):
    db_patient = db.query(Patient).filter(Patient.user_id == user_id).first()

    if not db_patient:
        return None

    update_data = patient.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_patient, key, value)

    db.commit()
    db.refresh(db_patient)
    return db_patient

def get_patient_details(db: Session):
    query = text("""
        SELECT 
            u.full_name,
            u.email,
            p.gender,
            p.date_of_birth,
            p.blood_group,
            p.address
        FROM users u
        JOIN patients p ON u.id = p.user_id
    """)

    result = db.execute(query).fetchall()
    return result