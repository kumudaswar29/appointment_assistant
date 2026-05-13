from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from app.database import Base


class Availability(Base):
    __tablename__ = "availability"

    id = Column(Integer, primary_key=True, index=True)
    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False)
    available_date = Column(Date, nullable=False)
    slot_time = Column(String(20), nullable=False)
    is_booked = Column(Boolean, default=False)