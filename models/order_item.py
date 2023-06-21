from sqlalchemy import String, func, Column, ForeignKey, DateTime, Text, Double, Integer
from sqlalchemy.orm import relationship

from .base import Base


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(String(191), primary_key=True, autoincrement=False, unique=True)
    order_id = Column(String(191), ForeignKey('orders.id'))
    menu_id = Column(String(191), ForeignKey('menus.id'))
    quantity = Column(Integer(), nullable=False)
    menu_price = Column(Double(), nullable=False)
    menu_extras = Column(Text(), nullable=True)

    order = relationship('Order', back_populates='order_items')
    menu = relationship('Menu')

    created_at = Column(DateTime, server_default=func.now(), nullable=True)
    updated_at = Column(DateTime, server_onupdate=func.now(), nullable=True)
    deleted_at = Column(DateTime, nullable=True)
