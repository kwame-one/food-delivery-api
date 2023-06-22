from pydantic import BaseModel, constr, EmailStr


class RestaurantRequest(BaseModel):
    name: constr(strip_whitespace=True, min_length=1)
    email: EmailStr
    address: constr(strip_whitespace=True, min_length=1)
    phone: constr(strip_whitespace=True, min_length=1)
    user_name: constr(strip_whitespace=True, min_length=1)
    user_email: EmailStr
