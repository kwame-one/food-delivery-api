from sqlalchemy import String, func, Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(String(191), primary_key=True, autoincrement=False, unique=True)
    name = Column(String(191), nullable=False)
    email = Column(String(191), nullable=False)
    address = Column(String(191), nullable=False)
    phone = Column(String(191), nullable=False)
    user_id = Column(String(191), ForeignKey('users.id'))

    created_at = Column(DateTime, server_default=func.now(), nullable=True)
    updated_at = Column(DateTime, server_onupdate=func.now(), nullable=True)
    deleted_at = Column(DateTime, nullable=True)

    menus = relationship('Menu', back_populates='restaurant')
    user = relationship('User')

    def __repr__(self):
        return f"Restaurant(id={self.id}, name={self.name}, email={self.email}, address={self.address}, phone={self.phone})"
