from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json() == {
        "status": "ok",
        "version": 2,
        "message": "Hello from CI/CD!",
    }


def test_add_route():
    client = app.test_client()
    response = client.get("/add?a=2&b=3")
    assert response.get_json() == {"result": 5.0}