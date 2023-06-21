from sqlalchemy import String, func, Column, DateTime
from sqlalchemy.orm import relationship

from .base import Base


class Role(Base):
    __tablename__ = "roles"

    id = Column(String(191), primary_key=True, autoincrement=False, unique=True)
    name = Column(String(191), nullable=False)
    users = relationship('User', back_populates='role')
    created_at = Column(DateTime, server_default=func.now(), nullable=True)
    updated_at = Column(DateTime, server_onupdate=func.now(), nullable=True)
    deleted_at = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"Role(id={self.id}, name={self.name})"
