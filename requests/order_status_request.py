from pydantic import BaseModel, validator, constr

from repositories.order_status_repository import OrderStatusRepository


class OrderStatusRequest(BaseModel):
    order_status_id: constr(strip_whitespace=True, min_length=1)

    @validator('order_status_id')
    def validate_status(cls, v):
        order_status_repo = OrderStatusRepository()
        order_status = order_status_repo.find(v)

        if order_status is None:
            raise ValueError('order status is invalid')
        return v