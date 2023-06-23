from sqlalchemy import delete, select

from configs.database import db_session
from models import MenuExtra
from repositories.base_repository import BaseRepository


class MenuExtraRepository(BaseRepository):
    def __init__(self):
        super().__init__(model=MenuExtra)

    def delete_by_menu_id(self, menu_id):
        db_session.execute(delete(self.model).where(self.model.menu_id == menu_id))
        db_session.commit()

    def find_by_menu_id_and_id(self, menu_id, id):
        return db_session.scalars(
            select(self.model).where(self.model.menu_id == menu_id).where(self.model.id == id)
        ).first()

    def find_by_id_in(self, ids):
        return db_session.scalars(select(self.model).where(self.model.id.in_(ids))).all()
