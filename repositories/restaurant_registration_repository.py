from models.restaurant_registration import RestaurantRegistration
from repositories.base_repository import BaseRepository


class RestaurantRegistrationRepository(BaseRepository):
    def __init__(self):
        super().__init__(model=RestaurantRegistration)
