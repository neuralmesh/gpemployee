import json
from fastapi.testclient import TestClient
from src import api

client = TestClient(api.app)

def test_read_root(mocker):
    mocker.patch("src.responsegetter.get_preprompt", return_value="give shortest possible answer")
    
    response = client.get("/")
    assert response.status_code == 200

