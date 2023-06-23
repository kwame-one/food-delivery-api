from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from dtos.order_item_dto import OrderItemDto
from dtos.order_status_dto import OrderStatusDto
from dtos.restaurant_dto import RestaurantDto
from dtos.user_dto import UserDto


class OrderDetailDto(BaseModel):
    id: str
    order_number: str
    total: float
    restaurant: RestaurantDto
    order_status: OrderStatusDto
    user: UserDto
    order_items: list[OrderItemDto]
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
