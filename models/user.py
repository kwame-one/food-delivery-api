from sqlalchemy import String, func, Column, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from .base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String(191), primary_key=True, autoincrement=False, unique=True)
    name = Column(String(191), nullable=False)
    email = Column(String(191), nullable=False)
    password = Column(String(191), nullable=False)
    role_id = Column(String(191), ForeignKey('roles.id'))
    role = relationship('Role', back_populates='users')

    created_at = Column(DateTime, server_default=func.now(), nullable=True)
    updated_at = Column(DateTime, server_onupdate=func.now(), nullable=True)
    deleted_at = Column(DateTime, nullable=True)
