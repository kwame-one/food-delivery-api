from pydantic import BaseModel, conlist

from requests.cart_item_request import CartItemRequest


class OrderRequest(BaseModel):
    cart_items: conlist(item_type=CartItemRequest, min_items=1)
