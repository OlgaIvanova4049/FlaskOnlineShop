from pydantic import BaseModel


class ProductSchema(BaseModel):
    id: int
    name: str
    description: str
    category_id: int
    quantity: int
    price: int
