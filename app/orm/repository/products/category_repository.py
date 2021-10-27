from app.orm.models.product.category_model import CategoryModel
from app.orm.repository.base import BaseRepository, session_scope
from app.orm.schemas.response.product.category_response import CategoryResponseSchema


class CategoryRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.model = CategoryModel

    def find_all_categories(self):
        with session_scope() as session:
            # nested_categories = session.query(self.model.nested_categories)
            # print(type(nested_categories))
            categories = session.query(self.model).all()
            #TODO: Something wrong
            res = [CategoryResponseSchema.from_orm(category).dict() for category in categories]
            return res






