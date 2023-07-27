from api.app import app
from fastapi import Response, status
from api.order.models import CreateOrderRequest, CreateOrderResponse

dummy_order = {
        "id": "order123"
    }

@app.get("/orders")
async def get_orders():
    return dummy_order

@app.post("/orders", response_model=CreateOrderResponse)
async def create_order(order: CreateOrderRequest, response: Response):
    response.status_code = status.HTTP_201_CREATED
    return dummy_order

@app.get("/orders/{order_id}")
async def get_order(order_id, response: Response):
    if order_id != "order123":
        response.status_code = status.HTTP_404_NOT_FOUND
        return

    return dummy_order

