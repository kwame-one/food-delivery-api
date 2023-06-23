from models import Order
from repositories.base_repository import BaseRepository


class OrderRepository(BaseRepository):
    def __init__(self):
        super().__init__(model=Order)
