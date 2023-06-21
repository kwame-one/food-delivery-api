from sqlalchemy import select

from configs.database import db_session
from models import User
from repositories.base_repository import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(model=User)

    def find_by_email(self, email):
        return db_session.scalars(select(self.model).where(self.model.email == email)).first()
