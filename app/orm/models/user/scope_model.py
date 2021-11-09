from sqlalchemy import Column, String, ForeignKey, Table, Integer
from sqlalchemy.orm import relationship

from app.orm.models.base import BaseIDModel, Base

usr_role_scope = Table('Role_Scope',
    Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('RoleId', Integer, ForeignKey('usr_role.id')),
    Column('ScopeId', Integer, ForeignKey('usr_scope.id')))


class RoleModel(BaseIDModel):
    __tablename__ = 'usr_role'

    name = Column(String, unique=True, nullable=False)
    scope = relationship(
        "ScopeModel",
        secondary=usr_role_scope,
        back_populates="role")

class ScopeModel(BaseIDModel):
    __tablename__ = 'usr_scope'

    name = Column(String, unique=True, nullable=False)
    role = relationship(
        "RoleModel",
        secondary=usr_role_scope,
        back_populates="scope")


