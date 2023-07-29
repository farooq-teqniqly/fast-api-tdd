from datetime import datetime

from api.app import app
from fastapi import Response, status, HTTPException
from api.order.models import CreateOrderRequest, CreateOrderResponse, GetOrderResponse
from typing import List
from api.app import order_repository


@app.get("/orders", response_model=List[GetOrderResponse])
async def get_orders():
    orders = order_repository.get_orders()
    return [GetOrderResponse(**order.dict()) for order in orders]

@app.post("/orders", response_model=CreateOrderResponse)
async def create_order(request: CreateOrderRequest, response: Response):
    new_order = order_repository.new_order(request)
    response.status_code = status.HTTP_201_CREATED
    return CreateOrderResponse(**new_order.dict())

@app.get("/orders/{order_id}", response_model=GetOrderResponse)
async def get_order(order_id):
    order = order_repository.get_order(order_id)

    if order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return GetOrderResponse(**order.dict())

