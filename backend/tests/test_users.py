from fastapi import status


def test_get_current_user(test_client, user_token):
    response = test_client.get(
        "/users/me",
        headers={
            "Authorization": f"Bearer {user_token}"
        },
    )

    assert response.status_code == status.HTTP_200_OK