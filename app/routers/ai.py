from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.dependencies import get_db
from app.crud.ai_match import auto_book_by_symptoms

router = APIRouter(prefix="/ai", tags=["AI Matching"])


class AutoBookInput(BaseModel):
    patient_id: int
    symptoms: str


@router.post("/auto-book")
def ai_auto_book(data: AutoBookInput, db: Session = Depends(get_db)):
    return auto_book_by_symptoms(db, data.patient_id, data.symptoms)