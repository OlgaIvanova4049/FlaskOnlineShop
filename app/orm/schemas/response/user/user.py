from pydantic import BaseModel


class UserSchemaResponse(BaseModel):
    id: int
    email: str

    class Config:
        orm_mode = True
