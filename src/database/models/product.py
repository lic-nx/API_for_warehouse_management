import uuid
from database.base import Base
from datetime import datetime
from alembic import op
import enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    String,
    Integer,
    Table,
    ForeignKey,
    DECIMAL,
    Boolean,
    Enum,
    JSON,
    DateTime,
    ARRAY,
    Float,
    CheckConstraint
)


# Определяем перечисление для статусов заказа
class OrderStatus(str, enum.Enum):
    START = "начало работы"
    IN_PROCESS = "в процессе"
    SHIPPED = "отправлен"
    DELIVERED = "доставлен"
    FAIL = "провалено"
    
# Определяем модель Product
class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    count = Column(Integer, CheckConstraint('count >= 0') ,nullable=False)


# Определяем модель Order
class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    status = Column(Enum(OrderStatus), nullable=False)
    order_items = relationship("OrderItem", back_populates="order")

# Определяем модель OrderItem
class OrderItem(Base):
    __tablename__ = 'order_items'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    count = Column(Integer, nullable=False)
    order = relationship("Order", back_populates="order_items")
    product = relationship("Product")

