from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    existing_user = UserService.get_user_by_email(
        db,
        user.email,
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered.",
        )

    return UserService.create_user(db, user)