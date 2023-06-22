from pydantic import BaseModel, constr, EmailStr

from constants.restaurant_registration_status import RestaurantRegistrationStatus


class RestaurantRegistrationRequest(BaseModel):
    restaurant_name: constr(strip_whitespace=True, min_length=1)
    restaurant_email: constr(strip_whitespace=True, min_length=1)
    restaurant_phone: constr(strip_whitespace=True, min_length=1)
    restaurant_address: constr(strip_whitespace=True, min_length=1)
    user_name: constr(strip_whitespace=True, min_length=1)
    user_email: EmailStr

    class Config:
        min_anystr_length = 1


class UpdateRestaurantRegistrationRequest(BaseModel):
    approve: bool
