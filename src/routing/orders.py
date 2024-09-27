from fastapi import APIRouter, HTTPException, Query
from starlette.requests import Request
from starlette.responses import JSONResponse
from tst.src.schemas.orders_items import PostOrdersRequestSchema, GetOrdersRequestSchema
from database.db import get_db
from typing import List
from repository.orders import OrdersRepositoriy
from database.models.product import OrderStatus


router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("", 
    responses={400: {"description": "error input"}},
    description="Создание заказа",
    # response_model= CartsReturnSchema
)
async def create_order(request:PostOrdersRequestSchema): 
    service = OrdersRepositoriy(get_db)
    response = service.create(request)
    return response


@router.get("", 
    responses={400: {"description": "error"}},
    description="Вывести список всех заказов", 
    response_model=List[GetOrdersRequestSchema])
    # response_model= CartsReturnSchema
async def get_all_orders(): 
    service = OrdersRepositoriy(get_db)
    response = service.get_all_orders()
    product_schemas = [GetOrdersRequestSchema.from_orm(order) for order in response]
    return product_schemas


# получить запись по заказу с id 
@router.get("/{id}", 
    responses={400: {"description": "error"}},
    description="Вывести список всех заказов", 
   )
    # response_model= CartsReturnSchema
async def get_orders_on_id(id): 
    service = OrdersRepositoriy(get_db)
    response = service.get_orders_on_id(id)
    return response

@router.patch("/{id}/status",
              responses={400: {"description": "error"}},
    description="обновление статуса заказа")
async def update_status(id, status: OrderStatus = Query(...)): 
        if status not in OrderStatus:
            return HTTPException(status_code=400, detail="Invalid status")

        # Преобразование строки в элемент перечисления
        status_enum = OrderStatus(status)
        service = OrdersRepositoriy(get_db)
        response = service.update_status(id, status)
        return response