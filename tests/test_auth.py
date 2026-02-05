def test_register_and_login(client):
    res = client.post(
        "/auth/register", json={"email": "test@test.com", "password": "123456"}
    )
    assert res.status_code == 200
