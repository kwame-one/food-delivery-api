from sqlalchemy import select, desc

from configs.database import db_session
from models import Order
from repositories.base_repository import BaseRepository


class OrderRepository(BaseRepository):
    def __init__(self):
        super().__init__(model=Order)

    def find_by_restaurant_id(self, restaurant_id, query=None):
        return db_session.scalars(
            select(self.model).where(self.model.restaurant_id == restaurant_id).order_by(desc(self.model.id))
        ).all()

    def find_by_user_id(self, user_id, query=None):
        return db_session.scalars(
            select(self.model).where(self.model.user_id == user_id).order_by(desc(self.model.id))
        ).all()
