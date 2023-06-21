from sqlalchemy import String, func, Column, ForeignKey, DateTime, Text, Double
from sqlalchemy.orm import relationship

from .base import Base


class MenuExtra(Base):
    __tablename__ = "menu_extras"

    id = Column(String(191), primary_key=True, autoincrement=False, unique=True)
    menu_id = Column(String(191), ForeignKey('menus.id'))
    name = Column(String(191), nullable=False)
    price = Column(Double(), nullable=False)

    menu = relationship('Menu', back_populates='menu_extras')

    created_at = Column(DateTime, server_default=func.now(), nullable=True)
    updated_at = Column(DateTime, server_onupdate=func.now(), nullable=True)
    deleted_at = Column(DateTime, nullable=True)
