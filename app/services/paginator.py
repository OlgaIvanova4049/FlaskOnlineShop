from typing import Optional

from pydantic import BaseModel, validator


class Paginator(BaseModel):
    limit: Optional[int] = 50
    offset: Optional[int] = 0
    has_next: Optional[bool] = False
    has_previous: Optional[bool] = False
    total: Optional[int] = 0

    # @validator("has_previous", always=True)
    # def has_previous_result(cls, v, values, *kwargs):
    #     return values['offset'] !=0
    # #
    # @validator("has_next", pre=True, always=True)
    # def has_next_result(cls, v, values, *kwargs):
    #     return values['limit'] + values['offset'] < values['total']

paginator = Paginator()
#TODO: has_previous, has_next