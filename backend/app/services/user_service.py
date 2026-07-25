from sqlalchemy.orm import Session

from app.auth.hashing import hash_password
from app.models.user import User
from app.schemas.user import UserCreate


class UserService:

    @staticmethod
    def get_user_by_email(db: Session, email: str) -> User | None:
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    def create_user(db: Session, user: UserCreate) -> User:

        hashed_password = hash_password(user.password)

        db_user = User(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            password_hash=hashed_password,
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user