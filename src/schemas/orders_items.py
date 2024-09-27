from typing import List, Optional, Union
from datetime import datetime
from pydantic import BaseModel, Field, validator
#op.execute('Insert into status values(1, \'распределение\'),(2, \'идут работы\')')
from database.models.product import OrderStatus
# шаблон для товара 

class ProductSchema(BaseModel):
    id: Optional[int]
    name: str
    description: Optional[str]
    price: float
    count: Optional[int] = None # Make count optional
    class Config:
        orm_mode = True

# поля с информацией о заказе
class OrderItemSchema(BaseModel):
    id:int
    id_order:int
    id_product:int
    count: int
    class Config:
        orm_mode = True


# для создания заказа(и данных заказа) или его обновления
class PostOrdersRequestSchema(BaseModel):
    id_product:int
    count_product:Optional[int]
    status:Optional[str]
    class Config:
        orm_mode = True
        allow_population_by_field_name = True


# для получения информации о заказе
class GetOrdersRequestSchema(BaseModel):
    id:int # id заказа
    created_at:datetime # дата создания заказа
    status:str # статус заказа
    orderInfo: Optional[PostOrdersRequestSchema]
    product:Optional[ProductSchema]
    class Config:
        orm_mode = True
        allow_population_by_field_name = True

