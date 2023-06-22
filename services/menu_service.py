from abc import ABC

from injector import inject

from repositories.menu_extra_repository import MenuExtraRepository
from repositories.menu_repository import MenuRepository
from services.base_service import BaseService


class MenuService(BaseService, ABC):
    @inject
    def __init__(self, repository: MenuRepository, menu_extra_repo: MenuExtraRepository):
        super().__init__(repository)
        self.menu_extra_repo = menu_extra_repo

    def get_dto(self):
        pass
