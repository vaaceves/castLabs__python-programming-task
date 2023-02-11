import json
import jwt
from fastapi.testclient import TestClient
from .main import app, jwt_secret


def test_post_endpoint():
    """Test if the required keys are present in the x-my-jwt header"""
    client = TestClient(app)
    payload = {"key": "value"}
    response = client.post("/", headers={"content-type": "application/json"}, json=payload)
    assert response.status_code == 200

    response_json = response.json()
    assert response_json["data"] == "key=value"
    assert "x-my-jwt" in response_json["headers"].keys()

    decoded_jwt = jwt.decode(response_json["headers"]["x-my-jwt"], jwt_secret, algorithms=["HS512"])

    assert "user" in decoded_jwt
    assert "date" in decoded_jwt
    assert "iat" in decoded_jwt
    assert "jti" in decoded_jwt

