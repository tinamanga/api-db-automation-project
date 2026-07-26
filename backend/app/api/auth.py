from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.user import UserCreate, UserResponse,UserLogin, Token
from app.services.user_service import UserService
from app.auth.jwt import create_access_token
from fastapi.security import OAuth2PasswordRequestForm
from app.core.exceptions import ConflictException


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

# signup
@router.post(
    "/register",
    summary="Register a new user",
    description="Creates a new user account after validating the request.",
    response_model=UserResponse,
    status_code=201,
    responses={
        201: {"description": "User created successfully"},
        409: {"description": "Email already registered"},
    },

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
       raise ConflictException("Email already registered.")

    return UserService.create_user(db, user)

@router.post(
    "/login",
    summary="Authenticate user",
    description="Returns a JWT access token for a valid email and password.",
    response_model=Token,
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    authenticated_user = UserService.authenticate_user(
        db,
        form_data.username,
        form_data.password,
    )

    if authenticated_user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    access_token = create_access_token(
        {
            "sub": authenticated_user.email,
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }