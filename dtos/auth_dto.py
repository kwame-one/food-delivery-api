from pydantic import BaseModel

from dtos.role_dto import RoleDto


class AuthDto(BaseModel):
    id: str
    name: str
    email: str
    role: RoleDto
    access_token: str

    class Config:
        orm_mode = True
