from pydantic import BaseModel


class OrderRequestSchema(BaseModel):
    user_id = int
    total_price = int
