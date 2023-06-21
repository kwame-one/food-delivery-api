from pydantic import BaseModel


class RoleDto(BaseModel):
    id: str
    name: str