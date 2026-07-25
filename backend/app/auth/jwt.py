from datetime import datetime, timedelta, timezone

from jose import JWTError, jwt

from app.core.config import settings


def create_access_token(data: dict) -> str:
    """
    Create a JWT access token.
    """
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM,
    )

    return encoded_jwt


def verify_access_token(token: str):
    """
    Verify a JWT access token.
    """
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM],
        )
        return payload

    except JWTError:
        return None