import json
from typing import Optional

from app.orm.schemas.base_schema import BaseFilter, BaseSort, QueryParam, OrderEnum


class ProductFilter(BaseFilter):
    price_min: Optional[int]
    price_max: Optional[int]
    name: Optional[str]


class ProductSort(BaseSort):
    name: Optional[OrderEnum]
    price: Optional[OrderEnum]
    description: Optional[OrderEnum]


class ProductQueryParam(QueryParam):
    filter: Optional[ProductFilter]
    sort: Optional[ProductSort]

