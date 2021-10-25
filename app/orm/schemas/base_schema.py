import enum
import json
from typing import Optional

from pydantic import BaseModel, Field


class BaseFilter(BaseModel):
    id: Optional[int]



class OrderEnum(str, enum.Enum):
    ASC = "ASC"
    DESC = "DESC"


class BaseSort(BaseModel):
    id: Optional[OrderEnum]

    class Config:
        extra = "forbid"



class LimitOffsetPaginator(BaseModel):
    limit: Optional[int]=50
    offset: Optional[int]=0



class QueryParam(BaseModel):
    filter: Optional[BaseFilter]
    sort: Optional[BaseSort]
    paginator: LimitOffsetPaginator=Field(default_factory=LimitOffsetPaginator)


    @classmethod
    def as_obj(cls, schema):
        print(schema)
        return cls.parse_obj({key: json.loads(value) for key, value in schema.items()})

#TODO: сделать отдельный query param без пагинатора



