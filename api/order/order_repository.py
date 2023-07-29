from api.order.models import Order, CreateOrderRequest
from typing import List, Optional
from datetime import datetime

class OrderRepository:
    def __init__(self):
        self._dummy_order = {
            "id": "order123",
            "created": datetime(2023, 7, 28, 16, 38),
            "status": "in_progress"
        }

    def get_orders(self) -> List[Order]:
        orders = [Order(**self._dummy_order)]
        return orders

    def get_order(self, order_id: str) -> Optional[Order]:
        if order_id != self._dummy_order["id"]:
            return None

        return Order(**self._dummy_order)

    def new_order(self, request: CreateOrderRequest) -> Order:
        order = Order(id="order123", created=self._dummy_order["created"], **request.dict())
        return order