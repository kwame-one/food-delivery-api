from pydantic import BaseModel


class UserDto(BaseModel):
    id: str
    name: str
    email: str

    class Config:
        orm_mode = True
