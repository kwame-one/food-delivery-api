from sqlalchemy import String, func, Column, DateTime

from .base import Base


class RestaurantRegistration(Base):
    __tablename__ = "restaurant_registrations"

    id = Column(String(191), primary_key=True, autoincrement=False, unique=True)
    restaurant_name = Column(String(191), nullable=False)
    restaurant_email = Column(String(191), nullable=False)
    restaurant_phone = Column(String(191), nullable=False)
    restaurant_address = Column(String(191), nullable=False)
    user_name = Column(String(191), nullable=False)
    user_email = Column(String(191), nullable=False)
    status = Column(String(191), nullable=False)

    created_at = Column(DateTime, server_default=func.now(), nullable=True)
    updated_at = Column(DateTime, server_onupdate=func.now(), nullable=True)
    deleted_at = Column(DateTime, nullable=True)
