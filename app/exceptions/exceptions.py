from typing import Optional
from werkzeug.exceptions import HTTPException


class NotFoundException(HTTPException):
    code: int = 422
    name: str = 'Not Found'
    entity_name: str = "Entity"

    def __init__(self, entity_name: Optional[str] = None):
        super().__init__(f'{entity_name or self.entity_name} not found')

class EntityExistsException(HTTPException):
    code: int = 400
    name: str = 'Bad request'
    entity_name: str = "Entity"

    def __init__(self, entity_name: Optional[str] = None):
        super().__init__(f'{entity_name or self.entity_name} already exists')

class UserNotFoundException(NotFoundException):
    entity_name: str = 'User'


class ProductNotFoundException(NotFoundException):
    entity_name: str = 'Product'


class CartItemNotFoundException(NotFoundException):
    entity_name: str = "Cart item"

class OrderNotFoundException(NotFoundException):
    entity_name: str = "Order"

class CategoryNotFoundException(NotFoundException):
    entity_name: str = "Category"

class AccessDeniedException(HTTPException):
    code: int = 403
    name: str = "Forbidden"
    description: str = "Access Denied"

class QuantityNotEnoughException(HTTPException):
    code: int = 400
    description: str = "Product quantity is not enough"



class UserExistsException(EntityExistsException):
    entity_name = 'User'

class CategoryExistsException(EntityExistsException):
    entity_name = 'Category'

class ProductExistsException(EntityExistsException):
    entity_name = 'Product'
