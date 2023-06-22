from pydantic import BaseModel, validator, constr, confloat
from werkzeug.datastructures import FileStorage


class MenuExtraRequest(BaseModel):
    name: constr(strip_whitespace=True, min_length=1)
    price: confloat(gt=0)

    class Config:
        arbitrary_types_allowed = True
