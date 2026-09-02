from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

def test_predict_valid():
    r = client.post("/predict", json={"features": [5.1, 3.5, 1.4, 0.2]})
    assert r.status_code == 200
    body = r.json()
    assert "prediction" in body
    assert 0 <= body["confidence"] <= 1

def test_predict_invalid_length():
    r = client.post("/predict", json={"features": [1, 2]})
    assert r.status_code == 422

def test_predict_invalid_type():
    r = client.post("/predict", json={"features": "not-a-list"})
    assert r.status_code == 422