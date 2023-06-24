from sqlalchemy import select, desc
from sqlalchemy.orm import joinedload
from sqlalchemy.testing.plugin.plugin_base import options

from configs.database import db_session
from models import Menu
from repositories.base_repository import BaseRepository
from utils import get_offset


class MenuRepository(BaseRepository):
    def __init__(self):
        super().__init__(model=Menu)

    def find_all(self, query=None):
        db_query = select(self.model).order_by(desc(self.model.id)) \
            .options(joinedload(self.model.menu_category), joinedload(self.model.menu_extras))

        return self.__parse_query(db_query, query)

    def find_by_restaurant_id(self, restaurant_id, query=None):
        db_query = select(self.model) \
            .where(self.model.restaurant_id == restaurant_id) \
            .options(joinedload(self.model.menu_category), joinedload(self.model.menu_extras)).order_by(
            desc(self.model.id))

        return self.__parse_query(db_query, query)

    def find_by_id_in(self, ids):
        return db_session.scalars(select(self.model)
                                  .options(joinedload(self.model.menu_category))
                                  .where(self.model.id.in_(ids))).all()

    def __parse_query(self, db_query, query=None):
        if query is None:
            return db_session.scalars(db_query).unique().all()

        if query.get('menu_category_id', '') != '':
            db_query = db_query.where(self.model.menu_category_id == query['menu_category_id'])

        if query.get('price', '') != '':
            db_query = db_query.where(self.model.menu_category_id == query['price'])

        if query.get('name', '') != '':
            db_query = db_query.where(self.model.name.like(f"%{query['name']}%"))

        if query.get('description', '') != '':
            db_query = db_query.where(self.model.description.like(f"%{query['description']}%"))

        if query.get('per_page', 20) != '':
            per_page = int(query.get('per_page', 20))
            offset = get_offset(query.get('page', 1), per_page)
            db_query = db_query.offset(offset).limit(per_page)

        return db_session.scalars(db_query).unique().all()
