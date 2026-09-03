import pytest
from app import app, soma


def test_soma():
    assert soma(2, 3) == 5


def test_soma_negativos():
    assert soma(-1, -1) == -2


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_rota_raiz(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.data == b"ok"


def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "healthy"


def test_soma_endpoint(client):
    resp = client.get("/soma/4/6")
    assert resp.status_code == 200
    assert resp.get_json()["resultado"] == 10
