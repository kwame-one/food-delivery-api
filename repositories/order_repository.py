from sqlalchemy import select, desc
from sqlalchemy.orm import joinedload

from configs.database import db_session
from models import Order
from repositories.base_repository import BaseRepository
from utils import get_offset


class OrderRepository(BaseRepository):
    def __init__(self):
        super().__init__(model=Order)

    def find_all(self, query=None):
        db_query = select(self.model) \
            .options(joinedload(self.model.user), joinedload(self.model.order_status),
                     joinedload(self.model.restaurant)) \
            .order_by(desc(self.model.id))

        if query is not None:
            if query.get('restaurant_id', '') != '':
                db_query = db_query.where(self.model.restaurant_id == query['restaurant_id'])

            if query.get('user_id', '') != '':
                db_query = db_query.where(self.model.user_id == query['user_id'])

            db_query = self.__parse_query(db_query, query)

        return db_session.scalars(db_query).all()

    def find_by_restaurant_id(self, restaurant_id, query=None):
        db_query = select(self.model) \
            .options(joinedload(self.model.user), joinedload(self.model.order_status)) \
            .where(self.model.restaurant_id == restaurant_id) \
            .order_by(desc(self.model.id))

        if query is not None:

            if query.get('user_id', '') != '':
                db_query = db_query.where(self.model.user_id == query['user_id'])

            db_query = self.__parse_query(db_query, query)

        return db_session.scalars(db_query).all()

    def find_by_user_id(self, user_id, query=None):
        db_query = select(self.model) \
            .options(joinedload(self.model.user), joinedload(self.model.order_status)) \
            .where(self.model.user_id == user_id).order_by(desc(self.model.id)) \
            .order_by(desc(self.model.id))

        if query is not None:

            if query.get('restaurant_id', '') != '':
                db_query = db_query.where(self.model.restaurant_id == query['restaurant_id'])

            db_query = self.__parse_query(db_query, query)

        return db_session.scalars(db_query).all()

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

    def __parse_query(self, db_query, query=None):

        if query.get('order_number', '') != '':
            db_query = db_query.where(self.model.order_number == query['order_number'])

        if query.get('order_status_id', '') != '':
            db_query = db_query.where(self.model.order_status_id == query['order_status_id'])

        if query.get('per_page', 20) != '':
            per_page = int(query.get('per_page', 20))
            offset = get_offset(query.get('page', 1), per_page)
            db_query = db_query.offset(offset).limit(per_page)

        return db_query
