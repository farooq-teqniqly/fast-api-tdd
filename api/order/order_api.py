from datetime import datetime

from api.app import app
from fastapi import Response, status, HTTPException
from api.order.models import CreateOrderRequest, CreateOrderResponse, GetOrderResponse
from typing import List

dummy_order = {
        "id": "order123",
        "created": datetime(2023, 7, 28, 16, 38)
    }

@app.get("/orders", response_model=List[GetOrderResponse])
async def get_orders():
    return [GetOrderResponse(id=dummy_order["id"], created=dummy_order["created"])]

@app.post("/orders", response_model=CreateOrderResponse)
async def create_order(order: CreateOrderRequest, response: Response):
    response.status_code = status.HTTP_201_CREATED
    return CreateOrderResponse(id=dummy_order["id"], created=dummy_order["created"])

@app.get("/orders/{order_id}", response_model=GetOrderResponse)
async def get_order(order_id):
    if order_id != "order123":
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return GetOrderResponse(id=dummy_order["id"], created=dummy_order["created"])

