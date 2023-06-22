from models import Restaurant
from repositories.base_repository import BaseRepository


class RestaurantRepository(BaseRepository):
    def __init__(self):
        super().__init__(model=Restaurant)
