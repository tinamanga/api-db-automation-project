from fastapi import APIRouter, Depends

from app.auth.dependencies import get_current_user
from app.models.user import User
from app.schemas.user import UserUpdate, UserResponse
from app.auth.dependencies import ( get_current_admin,get_current_active_user,
)

from sqlalchemy.orm import Session
from app.database.session import get_db
from app.services.user_service import UserService
from uuid import UUID
from fastapi import HTTPException, status

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get(
    "/me",
    summary="Get current user",
    description="Returns the authenticated user's profile.",
    response_model=UserResponse,
)
def get_me(
    current_user: User = Depends(get_current_user),
):
    return current_user


@router.get(
    "/",
    response_model=list[UserResponse],
)
def get_all_users(
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin),
):
    return UserService.get_all_users(db)

@router.get(
    "/{user_id}",
    response_model=UserResponse,
)
def get_user(
    user_id: UUID,
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin),
):
    user = UserService.get_user_by_id(
        db,
        user_id,
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return user

@router.put(
    "/{user_id}",
    response_model=UserResponse,
)
def update_user(
    user_id: UUID,
    user_update: UserUpdate,
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin),
):
    user = UserService.get_user_by_id(
        db,
        user_id,
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return UserService.update_user(
        db,
        user,
        user_update,
    )