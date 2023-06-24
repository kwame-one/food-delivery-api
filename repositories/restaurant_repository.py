from sqlalchemy import select, desc

from configs.database import db_session
from models import Restaurant
from repositories.base_repository import BaseRepository
from utils import get_offset


class RestaurantRepository(BaseRepository):
    def __init__(self):
        super().__init__(model=Restaurant)

    def find_all(self, query=None):
        db_query = select(self.model).order_by(desc(self.model.id))
        if query is None:
            return db_session.scalars(db_query).all()

        if query.get('name', '') != '':
            db_query = db_query.where(self.model.name.like(f"%{query['name']}%"))

        if query.get('phone', '') != '':
            db_query = db_query.where(self.model.phone.like(f"%{query['phone']}%"))

        if query.get('address', '') != '':
            db_query = db_query.where(self.model.address.like(f"%{query['address']}%"))

        if query.get('email', '') != '':
            db_query = db_query.where(self.model.email.like(f"%{query['email']}%"))

        if query.get('per_page', 20) != '':
            per_page = int(query.get('per_page', 20))
            offset = get_offset(query.get('page', 1), per_page)
            db_query = db_query.offset(offset).limit(per_page)

        return db_session.scalars(db_query).all()
