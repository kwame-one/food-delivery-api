from injector import Module, singleton, provider

from repositories.menu_extra_repository import MenuExtraRepository
from repositories.menu_repository import MenuRepository
from repositories.restaurant_repository import RestaurantRepository
from repositories.role_repository import RoleRepository
from repositories.user_repository import UserRepository
from services.menu_service import MenuService
from services.restaurant_service import RestaurantService


class MenuModule(Module):

    @singleton
    @provider
    def provide_menu_repository(self) -> MenuRepository:
        return MenuRepository()

    @singleton
    @provider
    def provide_menu_service(self,
                             repository: MenuRepository,
                             menu_extra_repo: MenuExtraRepository) -> MenuService:
        return MenuService(
            repository=repository,
            menu_extra_repo=menu_extra_repo)
