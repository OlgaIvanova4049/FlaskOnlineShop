from pydantic import BaseModel


class CartItemSchema(BaseModel):
    id: int
    cart_id: int
    product_id: int
    price: int
    quantity: int