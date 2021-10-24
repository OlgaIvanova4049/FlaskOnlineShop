import enum
import json
from typing import Optional

from pydantic import BaseModel


class BaseFilter(BaseModel):
    id: Optional[int]

    class Config:
        extra = "forbid"


class OrderEnum(str, enum.Enum):
    ASC = "ASC"
    DESC = "DESC"


class BaseSort(BaseModel):
    id: Optional[OrderEnum]

    class Config:
        extra = "forbid"


class QueryParam(BaseModel):
    filter: Optional[BaseFilter]
    sort: Optional[BaseSort]


    @classmethod
    def as_obj(cls, schema):
        print(schema)
        return cls.parse_obj({key: json.loads(value) for key, value in schema.items()})



