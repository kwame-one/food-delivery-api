from models import MenuExtra
from repositories.base_repository import BaseRepository


class MenuExtraRepository(BaseRepository):
    def __init__(self):
        super().__init__(model=MenuExtra)
