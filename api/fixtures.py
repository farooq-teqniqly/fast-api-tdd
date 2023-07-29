import pytest
from fastapi.testclient import  TestClient
from api.app import app

@pytest.fixture(scope="module")
def test_client():
    client = TestClient(app, raise_server_exceptions=False)

    with client:
        yield client