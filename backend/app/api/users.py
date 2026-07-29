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
from fastapi import Query
from typing import Literal
from app.schemas.user import PaginatedUsersResponse

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
    response_model=PaginatedUsersResponse,
)

def get_users(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    search: str | None = None,
    role: str | None = None,
    sort_by: str = "created_at",
    order: Literal["asc", "desc"] = "desc",
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin),
):
    return UserService.get_all_users(
        db=db,
        page=page,
        limit=limit,
        search=search,
        role=role,
        sort_by=sort_by,
        order=order,
    )


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