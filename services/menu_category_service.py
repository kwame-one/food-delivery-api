from abc import ABC

from injector import inject

from dtos.menu_category_dto import MenuCategoryDto
from repositories.menu_category_repository import MenuCategoryRepository
from repositories.menu_extra_repository import MenuExtraRepository
from repositories.menu_repository import MenuRepository
from services.base_service import BaseService


class MenuCategoryService(BaseService, ABC):
    @inject
    def __init__(self, repository: MenuCategoryRepository):
        super().__init__(repository)

    def get_dto(self):
        return MenuCategoryDto
