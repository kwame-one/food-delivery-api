from abc import ABC

from injector import inject

from dtos.menu_category_dto import MenuCategoryDto
from dtos.order_status_dto import OrderStatusDto
from repositories.menu_category_repository import MenuCategoryRepository
from repositories.menu_extra_repository import MenuExtraRepository
from repositories.menu_repository import MenuRepository
from repositories.order_status_repository import OrderStatusRepository
from services.base_service import BaseService


class OrderStatusService(BaseService, ABC):
    @inject
    def __init__(self, repository: OrderStatusRepository):
        super().__init__(repository)

    def get_dto(self):
        return OrderStatusDto
