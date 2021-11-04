from contextlib import contextmanager
from typing import Type

from pydantic.main import BaseModel
from sqlalchemy import func

from app.core.extensions import db
from app.orm.models.base import BaseIDModel


@contextmanager
def session_scope():
    session = db.create_scoped_session(options={"autoflush": False, "expire_on_commit": False})
    try:
        yield session
    except:
        session.rollback()
        raise
    finally:
        session.close()


class BaseRepository:
    def __init__(self):
        self.model: Type[BaseIDModel] = BaseIDModel

    def count(self):
        with session_scope() as session:
            return session.query(func.count(self.model.id)).scalar()

    def create(self, schema: BaseModel) -> BaseIDModel:
        with session_scope() as session:
            entity = self.model(**schema.dict(exclude={"id"}))
            session.add(entity)
            session.commit()
            return entity

    def delete(self, id):
        with session_scope() as session:
            entity = session.query(self.model).get(id)
            session.delete(entity)
            session.commit()

    def find_all(self):
        with session_scope() as session:
            return session.query(self.model).all()

    def find(self, id):
        with session_scope() as session:
            return session.query(self.model).get(id)

    def update(self, id: int, schema: BaseModel) -> BaseIDModel:
        with session_scope() as session:
            session.query(self.model).filter_by(id=id).update(schema.dict(exclude_none=True))
            session.commit()
            return self.find(id)
