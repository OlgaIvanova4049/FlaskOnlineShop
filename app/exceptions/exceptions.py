from typing import Optional
from werkzeug.exceptions import HTTPException

class NotFoundException(HTTPException):
    entity_name: str = "Entity"

    def __init__(self, entity_name: Optional[str] = None):
        super().__init__(f'{entity_name or self.entity_name} not found')


class UserNotFoundException(NotFoundException):
    code: int = 404
    name: str = 'Not Found'
    entity_name: str = 'User'

