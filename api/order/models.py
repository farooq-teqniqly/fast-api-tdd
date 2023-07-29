from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import List

class Order(BaseModel):
    id: str
    created: datetime
    status: str

class GetOrderResponse(BaseModel):
    id: str
    created: datetime
    status: str

class CreateOrderRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    status: str

class CreateOrderResponse(BaseModel):
    id: str
    created: datetime
    status: str