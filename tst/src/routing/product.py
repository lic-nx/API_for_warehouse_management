from fastapi import APIRouter, HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse
from schemas.orders_items import ProductSchema
from database.db import get_db
from typing import List
from repository.product import ProductRepositoriy
from database.models.product import OrderStatus


router = APIRouter(prefix="/products", tags=["products"])
# Создание товара (POST /products).
@router.post("", 
    responses={400: {"description": "error input"}},
    description="Создание товара"
)
async def create_product(request:ProductSchema): 
    service = ProductRepositoriy(get_db)
    response = service.create_product(request)
    return response


# Получение списка товаров (GET /products).
@router.get("", 
    responses={400: {"description": "error"}},
    description="Вывести список всех товаров", 
    response_model=List[ProductSchema])
    # response_model= CartsReturnSchema
async def get_all_products(): 
    service = ProductRepositoriy(get_db)
    response = service.get_all_products()
    product_schemas = [ProductSchema.from_orm(product) for product in response]
    return product_schemas

# Получение информации о товаре по id (GET /products/{id}).
@router.get("/{id}", responses={
    200: {"description": "Successful update"},
    404: {"description": "Product not found"},
    400: {"description": "Bad request"}
})
async def get_products_on_id(id): 
    service = ProductRepositoriy(get_db)
    response = service.get_products_on_id(id)
    return response


# Обновление информации о товаре (PUT /products/{id}).
@router.put("/{id}",
    responses={400: {"description": "error"}},
    description="Обновление товара", 
    response_model=ProductSchema)
# Удаление товара (DELETE /products/{id}).
async def update_product(id, new_sett:ProductSchema):
    service = ProductRepositoriy(get_db)
    response = service.update_product(id, new_sett)
    return response


@router.delete("/products/{id}", description="удалить товар")
async def delete_product(id):
    service = ProductRepositoriy(get_db)
    response = service.delete_product(id)
    return response