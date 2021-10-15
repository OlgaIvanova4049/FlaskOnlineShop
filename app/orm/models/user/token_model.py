from orm.models.base import BaseIDModel
from sqlalchemy import Column, String, DateTime, Integer, ForeignKey, VARCHAR
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ARRAY
from datetime import timedelta
from core.constants import token_life_time_hours


class TokenModel(BaseIDModel):
    __tablename__ = 'usr_token'

    access_token = Column(String)
    refresh_token = Column(String)
    user_id = Column(Integer, ForeignKey('usr_user.id', ondelete='SET NULL'))
    scope = Column(ARRAY(VARCHAR))
    expired_at = Column(DateTime)
    # TODO метод вычисления даты, проверить док-ю
    # TODO лезу в юзера, достаю поле админ и в зависимости от него устанавливаю скоп

    user = relationship('UserModel', back_populates='token')

    def set_expired_at(self):
        self.expired_at = self.created_at + timedelta(hours=token_life_time_hours)
        return self.created_at
