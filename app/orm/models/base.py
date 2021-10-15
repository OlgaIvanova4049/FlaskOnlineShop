from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class BaseModel:
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())


class BaseIDModel(Base, BaseModel):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

