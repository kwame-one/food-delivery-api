from abc import ABC

from injector import inject

from repositories.restaurant_repository import RestaurantRepository
from services.base_service import BaseService


class RestaurantService(BaseService, ABC):
    @inject
    def __init__(self, repository: RestaurantRepository):
        super().__init__(repository)
        pass

    def get_dto(self):
        pass
