from app.orm.models.product.product_model import ProductModel
from app.orm.repository.base import BaseRepository, session_scope
from app.orm.schemas.base_schema import OrderEnum
from app.orm.schemas.query.product.product_query import ProductQueryParam
from sqlalchemy import asc, desc

FUNC_MAPPING = {
    OrderEnum.ASC: asc,
    OrderEnum.DESC: desc
}


class ProductRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.model = ProductModel

    def filtered_sorted_product_list(self, parameters: ProductQueryParam):
        with session_scope() as session:
            result = session.query(self.model)
            if parameters.filter:
                if parameters.filter.name:
                    result = result.filter(self.model.name.like(f'%{parameters.filter.name}%'))
                if parameters.filter.price:
                    if parameters.filter.price.min:
                        result = result.filter(self.model.price >= parameters.filter.price.min)
                    if parameters.filter.price.max:
                        result = result.filter(self.model.price <= parameters.filter.price.max)
            if sort_params := parameters.sort:
                result = result.order_by(*[FUNC_MAPPING.get(value)(field) for field, value in sort_params.dict(exclude_none=True).items()])
            return result.limit(parameters.paginator.limit).offset(parameters.paginator.offset).all()

    def products_in_category(self, category_id, parameters: ProductQueryParam):
        with session_scope() as session:
            products = session.query(self.model).filter(self.model.category_id==category_id)
            return products.limit(parameters.paginator.limit).offset(parameters.paginator.offset).all()


