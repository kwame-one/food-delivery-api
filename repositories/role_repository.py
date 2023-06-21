from models.role import Role
from repositories.base_repository import BaseRepository


class RoleRepository(BaseRepository):
    def __init__(self):
        super().__init__(model=Role)
