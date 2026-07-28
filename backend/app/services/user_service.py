from sqlalchemy.orm import Session

from app.auth.hashing import hash_password,verify_password

from sqlalchemy import or_
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

    @staticmethod
    def authenticate_user(
        db,
        email: str,
        password: str,
    ):
        user = UserService.get_user_by_email(db, email)

        if not user:
            return None

        if not verify_password(password, user.password_hash):
            return None

        return user

    @staticmethod
    def get_user_by_id(
        db: Session,
        user_id,
    ):
        return (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )



    @staticmethod
    def get_all_users(
        db: Session,
        page: int = 1,
        limit: int = 10,
        search: str | None = None,
        role: str | None = None,
    ):
        query = db.query(User)

        # Search by first name, last name or email
        if search:
            query = query.filter(
                or_(
                    User.first_name.ilike(f"%{search}%"),
                    User.last_name.ilike(f"%{search}%"),
                    User.email.ilike(f"%{search}%"),
                )
            )

        # Filter by role
        if role:
            query = query.filter(User.role == role)

        total = query.count()

        users = (
            query.offset((page - 1) * limit)
            .limit(limit)
            .all()
        )

        return {
            "total": total,
            "page": page,
            "limit": limit,
            "pages": (total + limit - 1) // limit,
            "users": users,
        }

    @staticmethod
    def get_user_by_id(db, user_id):
        return (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )

    @staticmethod
    def update_user(db, user, user_update):
        update_data = user_update.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(user, key, value)

        db.commit()
        db.refresh(user)

        return user