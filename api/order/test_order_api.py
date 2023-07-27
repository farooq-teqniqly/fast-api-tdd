from api.app import app
from api.fixtures import test_client
from fastapi import status
from api.order.order_api import dummy_order
from api.order.models import CreateOrderRequest
from fastapi.encoders import jsonable_encoder

def test_get_returns_order(test_client):
    response = test_client.get("/orders")
    assert response.json() == dummy_order

def test_get_returns_200(test_client):
    response = test_client.get("/orders")
    assert response.status_code == status.HTTP_200_OK

def test_get_by_id_returns_order(test_client):
    response = test_client.get(f"/orders/{dummy_order['id']}")
    assert response.json() == dummy_order

def test_when_order_id_not_found_return_404(test_client):
    response = test_client.get("/orders/foo")
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_post_returns_created_order(test_client):
    request = CreateOrderRequest()

    response = test_client.post("/orders", json=jsonable_encoder(request))
    assert response.json() == dummy_order

def test_post_returns_201(test_client):
    request = CreateOrderRequest()
    response = test_client.post("/orders", json=jsonable_encoder(request))
    assert response.status_code == status.HTTP_201_CREATED

def test_post_when_request_invalid_returns_400(test_client):
    request = CreateOrderRequest(id="order123")
    response = test_client.post("/orders", json=jsonable_encoder(request))
    assert response.status_code == status.HTTP_400_BAD_REQUEST