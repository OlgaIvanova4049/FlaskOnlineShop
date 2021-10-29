from typing import Optional


class NotFoundException(Exception):
    entity_name: str = "Entity"

    def __init__(self, entity_name: Optional[str] = None):
        super().__init__(f'{entity_name or self.entity_name} not found')


class UserNotFoundException(NotFoundException):
    entity_name: str = 'User'