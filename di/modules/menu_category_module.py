from injector import Module, singleton, provider

from models import MenuCategory
from repositories.menu_category_repository import MenuCategoryRepository
from repositories.menu_extra_repository import MenuExtraRepository
from repositories.menu_repository import MenuRepository
from repositories.restaurant_repository import RestaurantRepository
from repositories.role_repository import RoleRepository
from repositories.user_repository import UserRepository
from services.menu_category_service import MenuCategoryService
from services.menu_service import MenuService
from services.restaurant_service import RestaurantService


class MenuCategoryModule(Module):

    @singleton
    @provider
    def provide_menu_category_repository(self) -> MenuCategory:
        return MenuCategory()

    @singleton
    @provider
    def provide_menu_category_service(self, repository: MenuCategoryRepository) -> MenuCategoryService:
        return MenuCategoryService(repository=repository)
