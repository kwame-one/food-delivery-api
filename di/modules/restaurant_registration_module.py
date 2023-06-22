from injector import Module, singleton, provider

from repositories.restaurant_registration_repository import RestaurantRegistrationRepository
from repositories.restaurant_repository import RestaurantRepository
from repositories.role_repository import RoleRepository
from repositories.user_repository import UserRepository
from services.restaurant_registration_service import RestaurantRegistrationService


class RestaurantRegistrationModule(Module):

    @singleton
    @provider
    def provide_restaurant_registration_repository(self) -> RestaurantRegistrationRepository:
        return RestaurantRegistrationRepository()

    @singleton
    @provider
    def provide_restaurant_registration_service(self,
                                                restaurant_registration_repository: RestaurantRegistrationRepository,
                                                user_repo: UserRepository,
                                                restaurant_repo: RestaurantRepository,
                                                role_repo: RoleRepository) -> RestaurantRegistrationService:
        return RestaurantRegistrationService(
            repository=restaurant_registration_repository,
            user_repo=user_repo,
            restaurant_repo=restaurant_repo,
            role_repo=role_repo)
