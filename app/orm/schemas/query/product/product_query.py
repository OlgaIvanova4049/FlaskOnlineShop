from typing import Optional

from pydantic import Field

from app.orm.schemas.base_schema import BaseFilter, BaseSort, QueryParam, OrderEnum
from app.orm.schemas.response.product.product_response import Paginator


class PriceProductFilter(BaseFilter):
    min: Optional[int]
    max: Optional[int]


class ProductFilter(BaseFilter):
    price: Optional[PriceProductFilter]
    name: Optional[str]


class ProductSort(BaseSort):
    name: Optional[OrderEnum]
    price: Optional[OrderEnum]
    description: Optional[OrderEnum]


class ProductQueryParam(QueryParam):
    filter: Optional[ProductFilter]
    sort: Optional[ProductSort]
    paginator: Paginator = Field(default_factory=Paginator)
