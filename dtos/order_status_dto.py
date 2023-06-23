from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class OrderStatusDto(BaseModel):
    id: str
    name: str
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
