import json
from fastapi.testclient import TestClient
from src import api

client = TestClient(api.app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200

