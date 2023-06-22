from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from dtos.menu_category_dto import MenuCategoryDto
from dtos.menu_extra_dto import MenuExtraDto


class MenuDto(BaseModel):
    id: str
    menu_category: Optional[MenuCategoryDto]
    name: str
    description: str
    price: float
    menu_extras: Optional[list[MenuExtraDto]]
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
