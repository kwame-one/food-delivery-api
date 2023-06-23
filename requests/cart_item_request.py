from typing import Optional

from pydantic import BaseModel, conint, validator

from repositories.menu_extra_repository import MenuExtraRepository
from repositories.menu_repository import MenuRepository


class CartItemRequest(BaseModel):
    menu_id: str
    quantity: conint(gt=0)
    menu_extras: list[Optional[str]]

    @validator('menu_id')
    def menu_exists(cls, v):
        menu_repo = MenuRepository()
        menu = menu_repo.find(v)
        if menu is None:
            raise ValueError('menu does not exists')
        return v

    @validator('menu_extras', each_item=True)
    def extra_exists(cls, v, values):
        menu_extra_repo = MenuExtraRepository()
        menu_extra = menu_extra_repo.find_by_menu_id_and_id(menu_id=values.get('menu_id', ''), id=v)
        if menu_extra is None:
            raise ValueError('menu extra does not exists')
        return v
