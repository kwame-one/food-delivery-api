from sqlalchemy import String, func, Column, DateTime
from sqlalchemy.orm import relationship

from .base import Base


class MenuCategory(Base):
    __tablename__ = "menu_categories"

    id = Column(String(191), primary_key=True, autoincrement=False, unique=True)
    name = Column(String(191), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=True)
    updated_at = Column(DateTime, server_onupdate=func.now(), nullable=True)
    deleted_at = Column(DateTime, nullable=True)

    menus = relationship('Menu', back_populates='menu_category')

    def __repr__(self):
        return f"MenuCategory(id={self.id}, name={self.name}, created_at={self.created_at})"
