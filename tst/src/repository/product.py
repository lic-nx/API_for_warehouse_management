from typing import List
from database.models.product import *
from schemas.orders_items import ProductSchema 
from sqlalchemy.future import select
from sqlalchemy import and_, func, insert, update, join, delete, text
from sqlalchemy.orm import joinedload
from fastapi import FastAPI, HTTPException, Depends
from database.models.product import OrderStatus

class ProductRepositoriy:



    def __init__(self, get_db):
        self.get_db = get_db
        
# создание нового товара
    def create_product(self, product: ProductSchema):
        with self.get_db() as session:
            new_product = Product(
            name=product.name,
            description=product.description,
            price=product.price,
            count=product.count
        )
            session.add(new_product)
            session.commit()
            session.refresh(new_product)
        return new_product


# получение всех товаров
    def get_all_products(self):
        with self.get_db() as session:
            orders = session.query(Product).all()
        return orders
    
    # получение по id
    def get_products_on_id(self, id):
        with self.get_db() as session:
            order = session.query(Product).filter(Product.id == id).first()
            if not order:
                raise HTTPException(status_code=404, detail="Order not found")
        return order
# обновление товара
    def update_product(self,id, new_sett):
        with self.get_db() as session:
            db_product = session.query(Product).filter(Product.id == id).first()
            if not db_product:
                raise HTTPException(status_code=404, detail="Product not found")

            db_product.name = new_sett.name
            db_product.description = new_sett.description
            db_product.price = new_sett.price
            db_product.count = new_sett.count

            session.commit()
            session.refresh(db_product)
        return db_product
    
# удаление 

    def delete_product(self, id):
        with self.get_db() as session:
            db_product = session.query(Product).filter(Product.id == id).first()
            if not db_product:
                raise HTTPException(status_code=404, detail="Product not found")

            session.delete(db_product)
            session.commit()
        return db_product
