from injector import Module, singleton, provider

from repositories.restaurant_repository import RestaurantRepository
from repositories.role_repository import RoleRepository
from repositories.user_repository import UserRepository
from services.restaurant_service import RestaurantService


class RestaurantModule(Module):

    @singleton
    @provider
    def provide_restaurant_repository(self) -> RestaurantRepository:
        return RestaurantRepository()

    @singleton
    @provider
    def provide_restaurant_service(self,
                                   restaurant_repository: RestaurantRepository,
                                   user_repo: UserRepository,
                                   role_repo: RoleRepository) -> RestaurantService:
        return RestaurantService(
            repository=restaurant_repository,
            user_repo=user_repo,
            role_repo=role_repo)
