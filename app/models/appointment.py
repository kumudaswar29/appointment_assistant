from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, Time
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)

    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False)

    appointment_date = Column(DateTime, nullable=False)
    slot_time = Column(Time, nullable=True)
    status = Column(String(20), default="booked")  # booked, cancelled, completed

    reason = Column(String(255), nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    patient = relationship("Patient")
    doctor = relationship("Doctor")