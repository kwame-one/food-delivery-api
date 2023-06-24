from pydantic import BaseModel, constr, EmailStr, validator

from repositories.user_repository import UserRepository


class RestaurantRequest(BaseModel):
    name: constr(strip_whitespace=True, min_length=1)
    email: EmailStr
    address: constr(strip_whitespace=True, min_length=1)
    phone: constr(strip_whitespace=True, min_length=10)
    user_name: constr(strip_whitespace=True, min_length=1)
    user_email: EmailStr

    @validator('user_email')
    def email_exists(cls, v):
        user_repo = UserRepository()
        category = user_repo.find_by_email(v)
        if category is not None:
            raise ValueError('email already exists')
        return v