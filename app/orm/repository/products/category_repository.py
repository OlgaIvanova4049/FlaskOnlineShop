from app.orm.models.product.category_model import CategoryModel
from app.orm.repository.base import BaseRepository, session_scope


class CategoryRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.model = CategoryModel

    # def list_all_categories(self):
    #     with session_scope() as session:
    #         self.model.nested_categories = session.query.
    #         return session.query(self.model).all()




