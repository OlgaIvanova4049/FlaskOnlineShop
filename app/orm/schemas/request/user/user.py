from typing import Optional

from pydantic import BaseModel


class UserSchemaRequest(BaseModel):
    email: Optional[str]
    password: Optional[str]
