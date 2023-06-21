from sqlalchemy import String, func, Column, ForeignKey, DateTime, Text, Double
from sqlalchemy.orm import relationship

from .base import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(String(191), primary_key=True, autoincrement=False, unique=True)
    order_number = Column(String(191), nullable=False)
    user_order_id = Column(String(191), ForeignKey('user_orders.id'))
    user_id = Column(String(191), ForeignKey('users.id'))
    restaurant_id = Column(String(191), ForeignKey('restaurants.id'))
    order_status_id = Column(String(191), ForeignKey('order_statuses.id'))
    total = Column(Double(), nullable=False)

    user_order = relationship('UserOrder', back_populates='orders')
    user = relationship('User')
    restaurant = relationship('Restaurant')
    order_status = relationship('OrderStatus')
    order_items = relationship('OrderItem', back_populates='order')

    created_at = Column(DateTime, server_default=func.now(), nullable=True)
    updated_at = Column(DateTime, server_onupdate=func.now(), nullable=True)
    deleted_at = Column(DateTime, nullable=True)
