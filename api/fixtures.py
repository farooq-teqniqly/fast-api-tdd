import pytest
from fastapi.testclient import  TestClient
from api.app import app

@pytest.fixture(scope="module")
def test_client():
    client = TestClient(app)

    with client:
        yield client