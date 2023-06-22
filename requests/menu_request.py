from typing import Optional

from pydantic import BaseModel, constr, confloat, validator
from werkzeug.datastructures import FileStorage

from repositories.menu_category_repository import MenuCategoryRepository
from requests.menu_extra_request import MenuExtraRequest


class MenuRequest(BaseModel):
    menu_category_id: constr(strip_whitespace=True, min_length=1)
    name: constr(strip_whitespace=True, min_length=1)
    description: constr(strip_whitespace=True, min_length=1)
    price: confloat(gt=0)
    menu_extras: list[Optional[MenuExtraRequest]]

    @validator('menu_category_id')
    def menu_category_id_exists(cls, v):
        menu_category_repo = MenuCategoryRepository()
        category = menu_category_repo.find(v)
        if category is None:
            raise ValueError('menu category does not exists')
        return v

    class Config:
        arbitrary_types_allowed = True
