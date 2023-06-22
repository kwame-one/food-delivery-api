from pydantic import BaseModel, constr


class MenuCategoryRequest(BaseModel):
    name: constr(strip_whitespace=True, min_length=1)
