import pytest
from httpx import ASGITransport, AsyncClient
from app.main import app, db


@pytest.mark.asyncio
async def test_create_user_async(faker):
    db.clear()
    transport = ASGITransport(app=app)

    async with AsyncClient(transport=transport, base_url="http://test") as client:
        username = faker.user_name()
        age = faker.random_int(min=18, max=89)

        response = await client.post("/users", json={"username": username,
                                                         "age": age})

    assert response.status_code == 201

    data = response.json()

    assert "id" in data
    assert data["username"] == username
    assert data["age"] == age


@pytest.mark.asyncio
async def test_get_user_async(faker):
    db.clear()
    transport = ASGITransport(app=app)

    async with AsyncClient(transport=transport, base_url="http://test") as client:

        create_response = await client.post("/users", json={"username": faker.user_name(),
                                                            "age": faker.random_int(min=18, max=80)})

        user_id = create_response.json()["id"]
        response = await client.get(f"/users/{user_id}")

    assert response.status_code == 200
    assert response.json()["id"] == user_id


@pytest.mark.asyncio
async def test_get_no_user_async():
    db.clear()
    transport = ASGITransport(app=app)

    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/users/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}


@pytest.mark.asyncio
async def test_delete_user_async(faker):
    db.clear()
    transport = ASGITransport(app=app)

    async with AsyncClient(transport=transport,base_url="http://test") as client:
        create_response = await client.post("/users", json={"username": faker.user_name(),
                                                            "age": faker.random_int(min=18, max=80)})
        user_id = create_response.json()["id"]

        response = await client.delete(f"/users/{user_id}")

    assert response.status_code == 204


@pytest.mark.asyncio
async def test_delete_same_user_async(faker):
    db.clear()

    transport = ASGITransport(app=app)

    async with AsyncClient(transport=transport, base_url="http://test") as client:
        create_response = await client.post("/users",json={"username": faker.user_name(),
                                                           "age": faker.random_int(min=18, max=80)})

        user_id = create_response.json()["id"]

        first_response = await client.delete(f"/users/{user_id}")
        second_response = await client.delete(f"/users/{user_id}")

    assert first_response.status_code == 204
    assert second_response.status_code == 404

    assert second_response.json() == {"detail": "User not found"}


@pytest.mark.asyncio
async def test_create_user_invalid_age_async(faker):
    db.clear()

    transport = ASGITransport(app=app)

    async with AsyncClient(transport=transport,base_url="http://test") as client:

        response = await client.post("/users", json={"username": faker.user_name(),
                                                     "age": "invalid"})

    assert response.status_code == 422