from sqlalchemy.ext.hybrid import hybrid_property

from app.orm.models.base import BaseIDModel
from sqlalchemy import Column, String, DateTime, Integer, ForeignKey, VARCHAR
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ARRAY
from datetime import timedelta
from app.core.constants import token_life_time_hours


class TokenModel(BaseIDModel):
    __tablename__ = 'usr_token'

    access_token = Column(String)
    refresh_token = Column(String)
    user_id = Column(Integer, ForeignKey('usr_user.id', ondelete='SET NULL'))
    scope = Column(ARRAY(VARCHAR))
    expired_at = Column(DateTime)

    # TODO лезу в юзера, достаю поле админ и в зависимости от него устанавливаю скоп
    # @hybrid_property
    # def expired_at(self):
    #     return self.expired_at

    # @expired_at.setter
    # def expired_at(self, token_life_time=token_life_time_hours):
    #     self.expired_at = self.created_at + timedelta(hours=token_life_time)

    # @hybrid_property
    # def scope(self):
    #     return self.scope

    # @scope.setter
    # def set_scope(self):
    #     if self.user.admin:
    #         self.scope = ('create', 'update', 'delete')
    #     else:
    #         self.scope = ('read')
    #     return self.scope


