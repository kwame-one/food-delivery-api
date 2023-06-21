from sqlalchemy import String, func, Column, DateTime
from sqlalchemy.orm import relationship

from .base import Base


class OrderStatus(Base):
    __tablename__ = "order_statuses"

    id = Column(String(191), primary_key=True, autoincrement=False, unique=True)
    name = Column(String(191), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=True)
    updated_at = Column(DateTime, server_onupdate=func.now(), nullable=True)
    deleted_at = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"OrderStatus(id={self.id}, name={self.name})"
