from sqlalchemy import select

from configs.database import db_session
from models.role import Role
from repositories.base_repository import BaseRepository


class RoleRepository(BaseRepository):
    def __init__(self):
        super().__init__(model=Role)

    def find_by_name(self, name):
        return db_session.scalars(select(self.model)
                                  .where(self.model.deleted_at == None)
                                  .where(self.model.name == name)).first()
