from sqlalchemy import select, desc
from sqlalchemy.orm import joinedload

from configs.database import db_session
from models import Menu
from repositories.base_repository import BaseRepository


class MenuRepository(BaseRepository):
    def __init__(self):
        super().__init__(model=Menu)

    def find_all(self, query=None):
        return db_session.scalars(
            select(self.model)
                .options(joinedload(self.model.menu_category), joinedload(self.model.menu_extras))
                .order_by(desc(self.model.id))
        ).unique().all()

    def find_by_restaurant_id(self, restaurant_id, query=None):
        return db_session.scalars(
            select(self.model)
                .where(self.model.restaurant_id == restaurant_id)
                .options(joinedload(self.model.menu_category), joinedload(self.model.menu_extras))
                .order_by(desc(self.model.id))
        ).unique().all()

    def find_by_id_in(self, ids):
        return db_session.scalars(select(self.model)
                                  .options(joinedload(self.model.menu_category))
                                  .where(self.model.id.in_(ids))).all()
