from pydantic import BaseModel, validator, constr, EmailStr

from repositories.user_repository import UserRepository


class RegisterRequest(BaseModel):
    name: constr(strip_whitespace=True, min_length=1)
    email: EmailStr
    password: constr(strip_whitespace=True, min_length=1)
    password_confirmation: constr(strip_whitespace=True, min_length=1)

    @validator('password_confirmation')
    def passwords_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError('passwords do not match')
        return v

    @validator('email')
    def email_exists(cls, v):
        user_repo = UserRepository()
        category = user_repo.find_by_email(v)
        if category is not None:
            raise ValueError('email already exists')
        return v
