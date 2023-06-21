from pydantic import BaseModel, validator, constr


class RegisterRequest(BaseModel):
    name: constr(strip_whitespace=True, min_length=1)
    email: constr(strip_whitespace=True, min_length=1)
    password: constr(strip_whitespace=True, min_length=1)
    password_confirmation: constr(strip_whitespace=True, min_length=1)

    @validator('password_confirmation')
    def passwords_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError('passwords do not match')
        return v
