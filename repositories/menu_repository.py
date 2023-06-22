from models import Menu
from repositories.base_repository import BaseRepository


class MenuRepository(BaseRepository):
    def __init__(self):
        super().__init__(model=Menu)
