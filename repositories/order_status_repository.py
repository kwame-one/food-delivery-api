from sqlalchemy import select

from configs.database import db_session
from models import MenuCategory, OrderStatus
from repositories.base_repository import BaseRepository


class OrderStatusRepository(BaseRepository):
    def __init__(self):
        super().__init__(model=OrderStatus)

    def find_by_name(self, name):
        return db_session.scalars(select(self.model).where(self.model.name == name)).first()