from app.orm.models.product.category_model import CategoryModel
from app.orm.repository.base import BaseRepository, session_scope
from app.orm.schemas.response.product.category_response import CategoryResponseSchema


class CategoryRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.model = CategoryModel

    def find_all_categories(self):
        with session_scope() as session:
            categories = session.query(self.model).all()
            #TODO: Something wrong
            res = [CategoryResponseSchema.from_orm(category) for category in categories]
            for model in res:
                all_parents = []
                parent = model.parent_object
                while parent:
                    all_parents.append(parent.name)
                    parent = parent.parent_object
                model.all_parents = sorted(all_parents)
            return res
