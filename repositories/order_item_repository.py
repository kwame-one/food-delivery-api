from models import OrderItem
from repositories.base_repository import BaseRepository


class OrderItemRepository(BaseRepository):
    def __init__(self):
        super().__init__(model=OrderItem)
