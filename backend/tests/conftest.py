import uuid

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.database.session import SessionLocal
from app.models.user import User


client = TestClient(app)


@pytest.fixture
def test_client():
    return client


@pytest.fixture
def user_payload():
    unique_email = f"test_{uuid.uuid4().hex}@example.com"

    return {
        "first_name": "Test",
        "last_name": "User",
        "email": unique_email,
        "password": "Password123",
    }


@pytest.fixture
def registered_user(test_client, user_payload):
    response = test_client.post(
        "/auth/register",
        json=user_payload,
    )

    assert response.status_code == 201

    return user_payload


@pytest.fixture
def user_token(test_client, registered_user):
    login = test_client.post(
        "/auth/login",
        data={
            "username": registered_user["email"],
            "password": registered_user["password"],
        },
    )

    assert login.status_code == 200

    return login.json()["access_token"]


@pytest.fixture
def admin_token(test_client):
    import uuid

    email = f"admin_{uuid.uuid4().hex}@example.com"

    payload = {
        "first_name": "Admin",
        "last_name": "User",
        "email": email,
        "password": "Password123",
    }

    # Register the user
    response = test_client.post(
        "/auth/register",
        json=payload,
    )

    assert response.status_code == 201

    # Promote to admin directly in the database
    db = SessionLocal()

    user = db.query(User).filter(User.email == email).first()

    user.role = "admin"

    db.commit()
    db.refresh(user)
    db.close()

    # Log in as admin
    login = test_client.post(
        "/auth/login",
        data={
            "username": email,
            "password": payload["password"],
        },
    )

    assert login.status_code == 200

    return login.json()["access_token"]