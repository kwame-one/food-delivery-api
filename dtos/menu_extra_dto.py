from typing import Optional

from pydantic import BaseModel

from dtos.menu_category_dto import MenuCategoryDto


class MenuExtraDto(BaseModel):
    id: str
    name: str
    price: float

    class Config:
        orm_mode = True
