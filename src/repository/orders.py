from typing import List
from database.models.product import *
from schemas.orders_items import PostOrdersRequestSchema 
from sqlalchemy.future import select
from sqlalchemy import and_, func, insert, update, join, delete, text
from sqlalchemy.orm import joinedload
from fastapi import FastAPI, HTTPException, Depends
from database.models.product import OrderStatus

class OrdersRepositoriy:
    status_model = Order
    services_model = OrderItem

    def __init__(self, get_db):
        self.get_db = get_db
        
# создание нового заказа
    def create(self, services: PostOrdersRequestSchema):
        with self.get_db() as session:
            product = session.query(Product).filter(Product.id == services.id_product).first()
            if not product or product.count < services.count_product:
                raise HTTPException(status_code=400, detail=f"Not enough stock for product {services.id_product}")
        # создаем запись. она сразу получет новый id и дату записи

            new_order = Order(status=OrderStatus(OrderStatus.START))
            session.add(new_order)
            session.commit()
            session.refresh(new_order)
        # заполняем недостоющие поля такие как заказанный товар и его кол-во
            product = session.query(Product).filter(Product.id == services.id_product).first()
            product.count -= services.count_product
            new_order_item = OrderItem(order_id=new_order.id, product_id=services.id_product, count=services.count_product)
            session.add(new_order_item)
            session.commit()
        return services


# вернуть все записи по заказам
    def get_all_orders(self):
        with self.get_db() as session:
            orders = session.query(Order).all()
        return orders
    

# вернуть запись по id
    def get_orders_on_id(self, id):
        with self.get_db() as session:
            order = session.query(Order).filter(Order.id == id).options(
            joinedload(Order.order_items).joinedload(OrderItem.product)
            ).first()
            if not order:
                raise HTTPException(status_code=404, detail="Order not found")
        return order
    
# обновить запись по id    
    def update_status(self, id, status:OrderStatus):
        with self.get_db() as session:
            order = session.query(Order).filter(Order.id == id).first()
            if not order:
                raise HTTPException(status_code=404, detail="Order not found")

            order.status = status
            session.commit()
            session.refresh(order)
        return order