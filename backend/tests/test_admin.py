from fastapi import status


def test_admin_dashboard(test_client, admin_token):
    response = test_client.get(
        "/admin/dashboard",
        headers={
            "Authorization": f"Bearer {admin_token}",
        },
    )

    assert response.status_code == status.HTTP_200_OK

    data = response.json()

    assert data["role"] == "admin"