def test_register_and_login(client):
    register = client.post(
        "/api/v1/auth/register", json={"email": "user@test.com", "password": "123456"}
    )
    assert register.status_code == 200

    login = client.post(
        "/api/v1/auth/login", json={"email": "user@test.com", "password": "123456"}
    )
    assert login.status_code == 200
    assert "access_token" in login.json()
