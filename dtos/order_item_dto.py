from datetime import datetime
from typing import Optional, Any

from pydantic import BaseModel


class OrderItemDto(BaseModel):
    id: str
    quantity: int
    menu_price: float
    menu_extras: Any
    menu: Any
    created_at: Optional[datetime]