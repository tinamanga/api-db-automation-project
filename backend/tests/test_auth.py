from fastapi import status


def test_register_user(test_client, user_payload):
    response = test_client.post(
        "/auth/register",
        json=user_payload,
    )

    assert response.status_code == status.HTTP_201_CREATED

    data = response.json()

    assert data["email"] == user_payload["email"]
    assert data["first_name"] == user_payload["first_name"]


def test_duplicate_email(test_client, registered_user):
    response = test_client.post(
        "/auth/register",
        json=registered_user,
    )

    assert response.status_code == status.HTTP_409_CONFLICT
    data = response.json()

    assert data["success"] is False
    assert data["error"] == "Email already registered."

    
def test_login(test_client, registered_user):
    response = test_client.post(
        "/auth/login",
        data={
            "username": registered_user["email"],
            "password": registered_user["password"],
        },
    )

    assert response.status_code == status.HTTP_200_OK

    token = response.json()

    assert "access_token" in token
    assert token["token_type"] == "bearer"


def test_get_current_user(test_client, user_token):
    response = test_client.get(
        "/users/me",
        headers={
            "Authorization": f"Bearer {user_token}",
        },
    )

    assert response.status_code == status.HTTP_200_OK