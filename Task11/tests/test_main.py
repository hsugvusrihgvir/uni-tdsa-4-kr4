import pytest
from app.main import db



@pytest.mark.parametrize(
    "user_id, expected_status",
    [
        (1, 200),
        (999, 404),
    ]
)
def test_get_user(client, user_id, expected_status):
    db.clear()

    client.post(
        "/users",
        json={"username": "dasha", "age": 20}
    )

    response = client.get(f"/users/{user_id}")

    assert response.status_code == expected_status

    if expected_status == 200:
        assert response.json() == {
            "id": 1,
            "username": "dasha",
            "age": 20
        }
    else:
        assert response.json() == {
            "detail": "User not found"
        }


@pytest.mark.parametrize(
    "username, age, expected_status",
    [
        ("dasha", 20, 201),
        ("masha", 25, 201),
        ("katya", "abc", 422),
    ]
)
def test_create_user(client, username, age, expected_status):
    db.clear()

    response = client.post(
        "/users",
        json={
            "username": username,
            "age": age
        }
    )

    assert response.status_code == expected_status

    if expected_status == 201:
        assert response.json()["username"] == username
        assert response.json()["age"] == age


def test_delete_user(client):
    db.clear()

    client.post(
        "/users",
        json={"username": "dasha", "age": 19}
    )

    response = client.delete("/users/1")

    assert response.status_code == 204


def test_delete_user_error(client):
    db.clear()

    response = client.delete("/users/999")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "User not found"
    }


def test_create_user_error(client):
    db.clear()

    response = client.post(
        "/users",
        json={"username": "dasha", "age": "invalid"}
    )

    assert response.status_code == 422