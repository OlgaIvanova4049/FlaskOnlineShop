from sqlalchemy import Column, String, DateTime, Integer, ForeignKey, VARCHAR
from sqlalchemy.dialects.postgresql import ARRAY

from app.orm.models.base import BaseIDModel


class TokenModel(BaseIDModel):
    __tablename__ = 'usr_token'

    access_token = Column(String)
    refresh_token = Column(String)
    user_id = Column(Integer, ForeignKey('usr_user.id', ondelete='SET NULL'))
    scope = Column(ARRAY(VARCHAR))
    expired_at = Column(DateTime)





