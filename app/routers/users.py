from fastapi import APIRouter, Depends
from app.utils.token import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/me")
def get_me(current_user=Depends(get_current_user)):
    return {
        "message": "Authorized user",
        "user": current_user
    }