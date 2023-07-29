from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from api.order.order_repository import OrderRepository

app = FastAPI()
order_repository = OrderRepository()

from api.order import order_api