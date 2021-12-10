import pytest
from flask.testing import FlaskClient
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_sync(client: FlaskClient):
    """should be a successful GET request"""
    resp = client.get('/sync')
    assert resp.status_code == 200
    assert isinstance(resp.json, dict)
    print("SYNC",resp.json)
    assert resp.json['output']['addition'] == 9
    assert resp.json['output']['multiply'] == 20

def test_async(client: FlaskClient):
    """should be a successful GET request"""
    resp = client.get('/async')
    assert resp.status_code == 200
    assert isinstance(resp.json, dict)
    print("ASYNC",resp.json)
    assert resp.json["output"]["addition"] == 9
    assert resp.json["output"]["multiply"] == 20