from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)

    gender = Column(String(10), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    blood_group = Column(String(5), nullable=True)
    address = Column(String(255), nullable=True)
    emergency_contact = Column(String(15), nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User")