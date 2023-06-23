from sqlalchemy import select

from configs.database import db_session
from models import Menu
from repositories.base_repository import BaseRepository


class MenuRepository(BaseRepository):
    def __init__(self):
        super().__init__(model=Menu)

    def find_by_id_in(self, ids):
        return db_session.scalars(select(self.model).where(self.model.id.in_(ids))).all()
