from pydantic import BaseModel, constr


class RestaurantRequest(BaseModel):
    name: constr(strip_whitespace=True, min_length=1)
    email: constr(strip_whitespace=True, min_length=1)
    address: constr(strip_whitespace=True, min_length=1)
    phone: constr(strip_whitespace=True, min_length=1)
    user_id: constr(strip_whitespace=True, min_length=1)
