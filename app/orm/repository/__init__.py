from app.orm.repository.carts.cart_item_repository import CartItemRepository
from app.orm.repository.carts.cart_repository import CartRepository
from app.orm.repository.orders.order_item_repository import OrderItemRepository
from app.orm.repository.orders.order_repository import OrderRepository
from app.orm.repository.products.category_repository import CategoryRepository
from app.orm.repository.products.product_repository import ProductRepository
from app.orm.repository.users.role_scope_repository import RoleRepository
from app.orm.repository.users.token_repository import TokenRepository
from app.orm.repository.users.user_repository import UserRepository


product_repository = ProductRepository()
user_repository = UserRepository()
category_repository = CategoryRepository()
cart_repository = CartRepository()
token_repository = TokenRepository()
cart_item_repository = CartItemRepository()
order_repository = OrderRepository()
order_item_repository = OrderItemRepository()
role_repository = RoleRepository()