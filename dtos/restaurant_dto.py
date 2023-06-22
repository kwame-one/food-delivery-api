from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class RestaurantDto(BaseModel):
    id: str
    name: str
    email: str
    phone: str
    address: str
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
