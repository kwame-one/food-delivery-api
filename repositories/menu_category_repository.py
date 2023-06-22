from models import MenuCategory
from repositories.base_repository import BaseRepository


class MenuCategoryRepository(BaseRepository):
    def __init__(self):
        super().__init__(model=MenuCategory)
