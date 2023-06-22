from injector import Module, singleton, provider

from repositories.restaurant_repository import RestaurantRepository
from services.restaurant_service import RestaurantService


class RestaurantModule(Module):

    @singleton
    @provider
    def provide_restaurant_repository(self) -> RestaurantRepository:
        return RestaurantRepository()

    @singleton
    @provider
    def provide_restaurant_service(self, restaurant_repository: RestaurantRepository) -> RestaurantService:
        return RestaurantService(repository=restaurant_repository)
