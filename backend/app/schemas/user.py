from uuid import UUID
from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "first_name": "Christina",
                "last_name": "Manga",
                "email": "christina@example.com",
                "password": "Christina123"
            }
        }
    }


class UserUpdate(BaseModel):
    first_name: str | None = Field(None, min_length=2, max_length=100)
    last_name: str | None = Field(None, min_length=2, max_length=100)
    role: str | None = None
    is_active: bool | None = None


class UserLogin(BaseModel):
    email: EmailStr
    password: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "email": "christina@example.com",
                "password": "Christina123"
            }
        }
    }


class UserResponse(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    email: EmailStr
    role: str
    is_active: bool



    model_config = {
        "from_attributes": True
    }
# for login purposes
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"