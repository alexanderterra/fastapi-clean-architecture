import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def auth_headers(client):
    # Register user
    client.post(
        "/api/v1/auth/register", json={"email": "test@test.com", "password": "123456"}
    )

    # Login user
    response = client.post(
        "/api/v1/auth/login", json={"email": "test@test.com", "password": "123456"}
    )

    token = response.json()["access_token"]

    return {"Authorization": f"Bearer {token}"}
