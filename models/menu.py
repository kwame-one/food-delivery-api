from sqlalchemy import String, func, Column, ForeignKey, DateTime, Text, Double
from sqlalchemy.orm import relationship

from .base import Base


class Menu(Base):
    __tablename__ = "menus"

    id = Column(String(191), primary_key=True, autoincrement=False, unique=True)
    menu_category_id = Column(String(191), ForeignKey('menu_categories.id'))
    restaurant_id = Column(String(191), ForeignKey('restaurants.id'))
    name = Column(String(191), nullable=False)
    description = Column(Text(), nullable=False)
    price = Column(Double(), nullable=False)
    image = Column(String(191), nullable=True)

    menu_category = relationship('MenuCategory', back_populates='menus')
    restaurant = relationship('Restaurant', back_populates='menus')
    menu_extras = relationship('MenuExtra', back_populates='menu')

    created_at = Column(DateTime, server_default=func.now(), nullable=True)
    updated_at = Column(DateTime, server_onupdate=func.now(), nullable=True)
    deleted_at = Column(DateTime, nullable=True)
