from sqlalchemy import select, desc

from configs.database import db_session
from models.restaurant_registration import RestaurantRegistration
from repositories.base_repository import BaseRepository
from utils import get_offset


class RestaurantRegistrationRepository(BaseRepository):
    def __init__(self):
        super().__init__(model=RestaurantRegistration)

    def find_all(self, query=None):
        db_query = select(self.model).order_by(desc(self.model.id))
        if query is None:
            return db_session.scalars(db_query).all()

        if query.get('status', '') != '':
            db_query = db_query.where(self.model.status == query['status'])

        if query.get('restaurant_phone', '') != '':
            db_query = db_query.where(self.model.restaurant_phone.like(f"%{query['restaurant_phone']}%"))

        if query.get('restaurant_email', '') != '':
            db_query = db_query.where(self.model.restaurant_email.like(f"%{query['restaurant_email']}%"))

        if query.get('user_name', '') != '':
            db_query = db_query.where(self.model.user_name.like(f"%{query['user_name']}%"))

        if query.get('user_email', '') != '':
            db_query = db_query.where(self.model.user_email.like(f"%{query['user_email']}%"))

        if query.get('per_page', 20) != '':
            per_page = int(query.get('per_page', 20))
            offset = get_offset(query.get('page', 1), per_page)
            db_query = db_query.offset(offset).limit(per_page)

        return db_session.scalars(db_query).all()
