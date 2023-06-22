from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from constants.restaurant_registration_status import RestaurantRegistrationStatus


class RestaurantRegistrationDto(BaseModel):
    id: str
    restaurant_name: str
    restaurant_email: str
    restaurant_phone: str
    restaurant_address: str
    user_name: str
    user_email: str
    status: RestaurantRegistrationStatus
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
