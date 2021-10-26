from app.orm.repository.orders.order_item_repository import OrderItemRepository
from app.orm.repository.orders.order_repository import OrderRepository
from app.orm.repository.products.category_repository import CategoryRepository
from app.orm.repository.products.product_repository import ProductRepository
from app.orm.repository.users.user_repository import UserRepository


product_repository = ProductRepository()
user_repository = UserRepository()
category_repository = CategoryRepository()