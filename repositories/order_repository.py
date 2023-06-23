from sqlalchemy import select, desc
from sqlalchemy.orm import joinedload

from configs.database import db_session
from models import Order
from repositories.base_repository import BaseRepository


class OrderRepository(BaseRepository):
    def __init__(self):
        super().__init__(model=Order)

    def find_all(self, query=None):
        return db_session.scalars(
            select(self.model)
                .options(joinedload(self.model.user), joinedload(self.model.order_status),
                         joinedload(self.model.restaurant))
                .order_by(desc(self.model.id))
        ).all()

    def find_by_restaurant_id(self, restaurant_id, query=None):
        return db_session.scalars(
            select(self.model)
                .options(joinedload(self.model.user), joinedload(self.model.order_status))
                .where(self.model.restaurant_id == restaurant_id)
                .order_by(desc(self.model.id))
        ).all()

    def find_by_user_id(self, user_id, query=None):
        return db_session.scalars(
            select(self.model)
                .options(joinedload(self.model.user), joinedload(self.model.order_status))
                .where(self.model.user_id == user_id).order_by(desc(self.model.id))
                .order_by(desc(self.model.id))
        ).all()

    def find_by_restaurant_id_and_id(self, restaurant_id, id):
        return db_session.scalars(
            select(self.model)
                .options(joinedload(self.model.user), joinedload(self.model.order_status),
                         joinedload(self.model.order_items))
                .where(self.model.restaurant_id == restaurant_id)
                .where(self.model.id == id)
        ).first()

    def find_by_user_id_and_id(self, user_id, id):
        return db_session.scalars(
            select(self.model)
                .options(joinedload(self.model.user), joinedload(self.model.order_status),
                         joinedload(self.model.order_items))
                .where(self.model.id == id)
                .where(self.model.user_id == user_id)
        ).first()
