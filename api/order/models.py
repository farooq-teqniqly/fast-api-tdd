from pydantic import BaseModel, Extra

class CreateOrderRequest(BaseModel):
    class Config:
        extra = Extra.forbid

class CreateOrderResponse(BaseModel):
    id: str