from sqlalchemy import String, func, Column, DateTime, Double
from sqlalchemy.orm import relationship

from .base import Base


class UserOrder(Base):
    __tablename__ = "user_orders"

    id = Column(String(191), primary_key=True, autoincrement=False, unique=True)
    user_id = Column(String(191), nullable=False)
    total = Column(Double(), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=True)
    updated_at = Column(DateTime, server_onupdate=func.now(), nullable=True)
    deleted_at = Column(DateTime, nullable=True)

    orders = relationship('Order', back_populates='user_order')

    def __repr__(self):
        return f"UserOrder(id={self.id}, user_id={self.user_id}, total={self.total}, created_at={self.created_at})"
