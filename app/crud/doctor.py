from sqlalchemy.orm import Session
from app.models.doctor import Doctor
from app.schemas.doctor import DoctorCreate, DoctorUpdate


# CREATE DOCTOR
def create_doctor(db: Session, doctor: DoctorCreate):
    existing = db.query(Doctor).filter(Doctor.user_id == doctor.user_id).first()

    if existing:
        return None  # prevents duplicate

    db_doctor = Doctor(**doctor.dict())
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor

# GET DOCTOR BY USER ID
def get_doctor_by_user_id(db: Session, user_id: int):
    return db.query(Doctor).filter(Doctor.user_id == user_id).first()


# UPDATE DOCTOR
def update_doctor(db: Session, user_id: int, doctor: DoctorUpdate):
    db_doctor = db.query(Doctor).filter(Doctor.user_id == user_id).first()

    if not db_doctor:
        return None

    for key, value in doctor.dict(exclude_unset=True).items():
        setattr(db_doctor, key, value)

    db.commit()
    db.refresh(db_doctor)
    return db_doctor